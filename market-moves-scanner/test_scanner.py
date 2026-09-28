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


if __name__ == "__main__":
    unittest.main()
