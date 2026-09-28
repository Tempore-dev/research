"""Offline tests for scanner.py using synthetic bars. Run:
    python3 -m unittest test_scanner.py
"""

import datetime as dt
import random
import unittest

import scanner as s

NOW = dt.datetime(2026, 9, 29, 14, 0, tzinfo=s.ET)   # a Tuesday
OPEN = NOW.replace(hour=9, minute=30)


def bars(closes, vols=None, first_open=None):
    ts = [int(OPEN.timestamp()) + 300 * i for i in range(len(closes))]
    opens = [first_open if first_open else closes[0]] + closes[:-1]
    return s.Bars(ts, opens, [max(o, c) for o, c in zip(opens, closes)],
                  [min(o, c) for o, c in zip(opens, closes)], closes,
                  vols or [1e6] * len(closes))


def daily(n=260, start=100.0, drift=0.0005, vol=0.015, seed=1):
    r = random.Random(seed)
    c = [start]
    for _ in range(n - 1):
        c.append(c[-1] * (1 + drift + r.gauss(0, vol)))
    return s.Bars(list(range(n)), c, c, c, c, [5e7] * n)


FLAT_SPY = bars([500 + 0.01 * (i % 2) for i in range(54)])


class ClassifyTests(unittest.TestCase):
    def test_gap_on_earnings_headline_is_news(self):
        closes = [90.0] + [90 + 0.05 * (i % 3) for i in range(53)]
        intraday = bars(closes, first_open=90.0)
        m = s.analyse_move("XYZ", "XYZ", intraday, daily(), FLAT_SPY,
                           100.0, 5e7, NOW)
        m.headlines = [{"title": "XYZ misses earnings, cuts guidance",
                        "publisher": "Wire", "link": "",
                        "ts": int(OPEN.timestamp()) - 3600}]
        v = s.classify(m, NOW)
        self.assertEqual(v.label, "News-driven")
        self.assertEqual(v.news_tone, "negative")
        r = s.rate(m, v, {}, daily())
        self.assertEqual(r.rating, "Hold")

    def test_steady_grind_without_news_is_automated_selling(self):
        closes = [100 - 0.09 * (i + 1) + (0.02 if i % 5 == 0 else 0)
                  for i in range(54)]
        intraday = bars(closes, vols=[1.3e6] * 54, first_open=100.0)
        m = s.analyse_move("ABC", "ABC", intraday, daily(), FLAT_SPY,
                           100.0, 4e7, NOW)
        self.assertLess(m.move_pct, -3)
        v = s.classify(m, NOW)
        self.assertEqual(v.label, "Automated/flow-driven selling")
        r = s.rate(m, v, {"forwardPE": 15, "trailingPE": 20,
                          "averageAnalystRating": "1.6 - Buy",
                          "marketCap": 5e11}, daily(drift=0.001))
        self.assertIn(r.rating, ("Buy", "Strong Buy"))

    def test_beta_move_counts_as_flow(self):
        spy = bars([500 * (1 - 0.0004 * i) for i in range(54)])
        stock = bars([100 * (1 - 0.0008 * i) for i in range(54)],
                     first_open=100.0)
        m = s.analyse_move("BET", "BET", stock, daily(), spy, 100.0, 5e7,
                           NOW)
        self.assertGreater(m.market_share, 0.5)
        self.assertTrue(s.classify(m, NOW).label.startswith("Automated"))


class HelperTests(unittest.TestCase):
    def test_rsi_bounds(self):
        self.assertEqual(s.rsi([float(i) for i in range(1, 40)]), 100.0)
        self.assertLess(s.rsi([float(i) for i in range(40, 1, -1)]), 5)

    def test_third_friday(self):
        self.assertEqual(s.third_friday(dt.date(2026, 9, 1)),
                         dt.date(2026, 9, 18))

    def test_keyword_match_is_whole_word(self):
        self.assertEqual(s.has(["cut"], "Execution shortcut"), [])
        self.assertEqual(s.has(["cut"], "Company to cut jobs"), ["cut"])

    def test_alert_dedup(self):
        m = s.analyse_move("ABC", "ABC", bars([96.0] * 10, first_open=96.0),
                           daily(), FLAT_SPY, 100.0, 5e7, NOW)
        v = s.Verdict("Mixed / unclear", 0, 0, 0, "none", [], [])
        r = s.Rating("Hold", 50, {})
        state = {}
        x = [{"move": m, "verdict": v, "rating": r}]
        self.assertEqual(len(s.new_signals(x, state, "d1")), 1)
        self.assertEqual(len(s.new_signals(x, state, "d1")), 0)
        self.assertEqual(len(s.new_signals(x, state, "d2")), 1)


def iso(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")


def alpaca_rows(b):
    return [{"t": iso(t), "o": o, "h": h, "l": l, "c": c, "v": v, "n": 1,
             "vw": c} for t, o, h, l, c, v in zip(*b.cols())]


class FakeAlpacaHTTP:
    """Serves Alpaca-format JSON (shapes from the official alpaca-py SDK)."""

    def __init__(self):
        self.calls = []
        closes = [100 - 0.09 * (i + 1) for i in range(54)]
        self.intraday = {"ABC": bars(closes, vols=[1.3e6] * 54,
                                     first_open=100.0),
                         "QUIET": bars([100.0] * 54), "SPY": FLAT_SPY}
        d = daily()
        # Daily bars end the day before the session, at midnight ET.
        day0 = OPEN.replace(hour=0, minute=0) - dt.timedelta(days=len(d.ts))
        d.ts = [int((day0 + dt.timedelta(days=i)).timestamp())
                for i in range(len(d.ts))]
        d.close[-1] = 100.0
        self.daily = d

    def __call__(self, url, headers=None, timeout=20, opener=None):
        import json, urllib.parse
        u = urllib.parse.urlsplit(url)
        q = dict(urllib.parse.parse_qsl(u.query))
        self.calls.append((u.path, q))
        if "news.google.com" in url or "yahoo" in url:
            raise s.FetchError(429, url)
        assert headers["APCA-API-KEY-ID"] == "k"
        if u.path == "/v1beta1/screener/stocks/most-actives":
            return json.dumps({"most_actives": [
                {"symbol": x, "volume": 1, "trade_count": 1}
                for x in ("SPY", "ABC", "QUIET")],
                "last_updated": "2026-09-29T18:00:00.123456789Z"}).encode()
        if u.path == "/v2/stocks/bars":
            syms = q["symbols"].split(",")
            if q["timeframe"] == "1Day":
                data = {x: alpaca_rows(self.daily) for x in syms}
            else:
                data = {x: alpaca_rows(self.intraday[x]) for x in syms}
            # Paginate: first page holds the first symbol only.
            if len(syms) > 1 and "page_token" not in q:
                return json.dumps({"bars": {syms[0]: data[syms[0]]},
                                   "next_page_token": "p2"}).encode()
            if "page_token" in q:
                data.pop(syms[0])
            return json.dumps({"bars": data,
                               "next_page_token": None}).encode()
        if u.path == "/v1beta1/news":
            return json.dumps({"news": [{
                "id": 1, "headline": "ABC CEO to resign", "source": "benzinga",
                "url": "https://x", "summary": "", "author": "", "content": "",
                "created_at": "2026-09-29T12:00:00.5Z",
                "updated_at": "2026-09-29T12:00:00Z",
                "symbols": ["ABC", "XYZ"]}],
                "next_page_token": None}).encode()
        raise AssertionError(url)


class AlpacaScanTests(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmp = tempfile.mkdtemp()
        self._cache, s.CACHE = s.CACHE, self.tmp
        self._get, self.fake = s.http_get, FakeAlpacaHTTP()
        s.http_get = self.fake

    def tearDown(self):
        s.CACHE, s.http_get = self._cache, self._get

    def test_scan_end_to_end(self):
        api = s.Alpaca("k", "secret", "iex")
        report, results = s.scan(NOW.astimezone(dt.timezone.utc), True, api)
        self.assertEqual([r["move"].symbol for r in results], ["ABC"])
        r = results[0]
        self.assertAlmostEqual(r["move"].move_pct, -4.86, places=2)
        self.assertEqual([h["title"] for h in r["move"].headlines],
                         ["ABC CEO to resign"])
        self.assertIsNone(r["rating"].factors["valuation"])
        self.assertIn("valuation n/a", report)
        self.assertIn("Alpaca most actives; iex feed", report)
        bar_calls = [q for p, q in self.fake.calls if p == "/v2/stocks/bars"]
        self.assertTrue(all(q["feed"] == "iex" for q in bar_calls))
        self.assertTrue(any(q.get("page_token") == "p2" for q in bar_calls))
        # Daily bars are cached: a second scan doesn't refetch them.
        n = sum(1 for q in bar_calls if q["timeframe"] == "1Day")
        s.scan(NOW.astimezone(dt.timezone.utc), True, api)
        n2 = sum(1 for p, q in self.fake.calls
                 if p == "/v2/stocks/bars" and q["timeframe"] == "1Day")
        self.assertEqual(n, n2)

    def test_closed_market_skips(self):
        api = s.Alpaca("k", "secret")
        sunday = dt.datetime(2026, 10, 4, 12, 0, tzinfo=s.ET)
        self.assertEqual(s.scan(sunday, False, api), ("", []))

    def test_missing_keys_explains_setup(self):
        with self.assertRaises(SystemExit) as e:
            s.Alpaca("", "")
        self.assertIn("--setup", str(e.exception))

    def test_parse_ts_nanoseconds(self):
        self.assertEqual(s.parse_ts("2026-09-29T13:30:00.123456789Z"),
                         int(dt.datetime(2026, 9, 29, 13, 30,
                                         tzinfo=dt.timezone.utc).timestamp()))


class NotificationTests(unittest.TestCase):
    def setUp(self):
        import tempfile
        self._reports, s.REPORTS = s.REPORTS, tempfile.mkdtemp()
        self._notify, self.sent = s.notify, []
        s.notify = lambda *a: self.sent.append(a)

    def tearDown(self):
        s.REPORTS, s.notify = self._reports, self._notify

    def signal(self, sym, move=-4.9, label="Automated/flow-driven selling"):
        m = s.analyse_move(sym, sym, bars([100 + move] * 10,
                                          first_open=100 + move),
                           daily(), FLAT_SPY, 100.0, 5e7, NOW)
        v = s.Verdict(label, 80, 10, 70, "none",
                      ["no catalyst headlines found"], [])
        return {"move": m, "verdict": v,
                "rating": s.Rating("Buy", 64.5, {})}

    def test_one_notification_per_signal(self):
        s.notify_signals([self.signal("ABC")], "latest.md")
        title, body, subtitle, path = self.sent[0]
        self.assertEqual(title, "ABC -4.9% → Buy")
        self.assertTrue(subtitle.startswith("Automated selling · $95.10"))
        self.assertEqual(body, "no catalyst headlines found")
        self.assertEqual(path, "latest.md")

    def test_news_signal_shows_headline(self):
        x = self.signal("XYZ", label="News-driven")
        x["verdict"].news_tone = "negative"
        x["verdict"].catalysts = [{"title": "XYZ cuts guidance", "ts": 0}]
        s.notify_signals([x], "latest.md")
        self.assertEqual(self.sent[0][1], "XYZ cuts guidance")
        self.assertIn("News-driven (negative news)", self.sent[0][2])

    def test_overflow_is_summarised(self):
        s.notify_signals([self.signal(f"S{i}") for i in range(7)], "l.md")
        self.assertEqual(len(self.sent), s.MAX_NOTIFICATIONS + 1)
        self.assertIn("3 more", self.sent[-1][0])

    def test_error_alert_once_per_day_and_rearmed(self):
        s.notify_error_once("HTTP 401")
        s.notify_error_once("HTTP 401")
        self.assertEqual(len(self.sent), 1)
        state_path = s.os.path.join(s.REPORTS, ".state.json")
        state = s.load_state(state_path)
        state.pop("error_notified")  # what a successful run does
        s.save_json(state_path, state)
        s.notify_error_once("HTTP 401")
        self.assertEqual(len(self.sent), 2)


class MacNotifyCommandTests(unittest.TestCase):
    def setUp(self):
        self.cmds = []
        self._run, self._plat = s.subprocess.run, s.sys.platform
        self._which = s._mac_notifier
        s.subprocess.run = lambda cmd, **k: self.cmds.append(cmd)
        s.sys.platform = "darwin"

    def tearDown(self):
        s.subprocess.run, s.sys.platform = self._run, self._plat
        s._mac_notifier = self._which

    def test_osascript_passes_text_as_arguments(self):
        s._mac_notifier = lambda: None
        title, body = 'NVDA -4.9% → Buy "quoted"', "a · b \\ c"
        s.notify(title, body, "sub", "/tmp/x.md")
        cmd = self.cmds[0]
        self.assertEqual(cmd[0], "osascript")
        self.assertEqual(cmd[-3:], [title, body, "sub"])
        script = " ".join(c for c in cmd[1:-3] if c != "-e")
        self.assertNotIn("NVDA", script)  # text never enters the script

    def test_terminal_notifier_opens_report(self):
        s._mac_notifier = lambda: "/opt/homebrew/bin/terminal-notifier"
        s.notify("T", "B", "S", "/tmp/r e.md")
        cmd = self.cmds[0]
        self.assertEqual(cmd[cmd.index("-open") + 1], "file:///tmp/r%20e.md")
        self.assertEqual(cmd[cmd.index("-subtitle") + 1], "S")

    def test_refused_terminal_notifier_falls_back_to_osascript(self):
        class Refused:
            returncode, stderr = 3, b"Notifications are not allowed"
        s._mac_notifier = lambda: "/opt/homebrew/bin/terminal-notifier"
        s.subprocess.run = lambda cmd, **k: (self.cmds.append(cmd),
                                             Refused())[1]
        s.notify("T", "B", "S", "/tmp/r.md")
        self.assertEqual([c[0] for c in self.cmds],
                         ["/opt/homebrew/bin/terminal-notifier", "osascript"])


class MacAlertTests(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.popens = []
        self._popen, self._plat = s.subprocess.Popen, s.sys.platform
        s.subprocess.Popen = lambda args, **k: self.popens.append((args, k))
        s.sys.platform = "darwin"
        self._reports, s.REPORTS = s.REPORTS, tempfile.mkdtemp()

    def tearDown(self):
        s.subprocess.Popen, s.sys.platform = self._popen, self._plat
        s.REPORTS = self._reports

    def test_one_alert_with_open_details_button(self):
        items = [(f"S{i} -4.9% → Buy", "Automated selling", 'says "hi"')
                 for i in range(8)]
        self.assertEqual(s.notify_items(items, "/tmp/latest.html"),
                         "macOS alert")
        self.assertEqual(len(self.popens), 1)
        args, kw = self.popens[0]
        title, text, path, button = args[-4:]
        self.assertEqual(title, "Market moves: 8 new signal(s)")
        self.assertIn('S0 -4.9% → Buy\nAutomated selling\nsays "hi"', text)
        self.assertTrue(text.endswith("…and 2 more"))
        self.assertEqual((path, button), ("/tmp/latest.html", "Open details"))
        self.assertTrue(kw["start_new_session"])
        script = " ".join(a for a in args[1:-4] if a != "-e")
        self.assertIn("giving up after 240", script)
        self.assertIn('do shell script "open " & quoted form of (item 3',
                      script)
        self.assertNotIn("S0", script)  # text only ever passed as arguments

    def test_error_alert_opens_log(self):
        s.notify_error_once("HTTP 401 Unauthorized")
        args, _ = self.popens[0]
        self.assertEqual(args[-1], "Open log")
        self.assertTrue(args[-2].endswith("scanner.log"))

    def test_banner_style_opt_in(self):
        sent = []
        orig = s.notify
        s.notify = lambda *a: sent.append(a) or "banner"
        s.os.environ["MAC_NOTIFY"] = "banner"
        try:
            s.notify_items([("T", "S", "B")], "/tmp/x.html")
        finally:
            s.notify = orig
            del s.os.environ["MAC_NOTIFY"]
        self.assertEqual(self.popens, [])
        self.assertEqual(sent, [("T", "B", "S", "/tmp/x.html")])


class HtmlReportTests(unittest.TestCase):
    def test_page_escapes_and_marks_new(self):
        m = s.analyse_move("A&B", "A&B <Corp>", bars([95.0] * 10,
                                                     first_open=95.0),
                           daily(), FLAT_SPY, 100.0, 5e7, NOW)
        v = s.Verdict("News-driven", 60, 70, 10, "negative", ["x < y"],
                      [{"title": "<b>Guidance cut</b>", "ts": 0,
                        "publisher": "Wire", "link": "https://e.com/?a=1&b=2"}])
        r = s.Rating("Hold", 40.0, {"valuation": None, "momentum": 55})
        page = s.render_html(NOW, "hdr", [{"move": m, "verdict": v,
                                           "rating": r}], {"A&B"})
        self.assertIn("A&amp;B &lt;Corp&gt;", page)
        self.assertIn("&lt;b&gt;Guidance cut&lt;/b&gt;", page)
        self.assertIn('href="https://e.com/?a=1&amp;b=2"', page)
        self.assertIn('class="card new"', page)
        self.assertIn("<td>n/a</td>", page)
        self.assertNotIn("<b>Guidance", page)

    def test_sample_page_renders(self):
        self.assertIn("NVDA", s.sample_page())


class PhoneCopyTests(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmp = tempfile.mkdtemp()
        self._icloud = s.ICLOUD
        self._env = s.os.environ.pop("PHONE_DIR", None)

    def tearDown(self):
        s.ICLOUD = self._icloud
        s.os.environ.pop("PHONE_DIR", None)
        if self._env is not None:
            s.os.environ["PHONE_DIR"] = self._env

    def test_copies_into_icloud_drive_when_present(self):
        s.ICLOUD = self.tmp
        s.copy_for_phone("<p>hi</p>")
        with open(s.os.path.join(self.tmp, "Market Moves",
                                 "latest.html")) as f:
            self.assertEqual(f.read(), "<p>hi</p>")

    def test_no_icloud_no_copy(self):
        s.ICLOUD = s.os.path.join(self.tmp, "missing")
        self.assertIsNone(s.phone_copy_dir())

    def test_phone_dir_override_and_off(self):
        s.os.environ["PHONE_DIR"] = self.tmp
        self.assertEqual(s.phone_copy_dir(), self.tmp)
        s.os.environ["PHONE_DIR"] = ""
        self.assertIsNone(s.phone_copy_dir())


if __name__ == "__main__":
    unittest.main()
