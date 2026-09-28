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


if __name__ == "__main__":
    unittest.main()
