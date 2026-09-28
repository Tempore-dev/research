#!/usr/bin/env python3
"""Large-move scanner for the most traded US stocks.

Runs on your own computer, every 5 minutes during US market hours
(install the schedule with `python3 scanner.py --install`). Each run:

1. Pull Yahoo Finance's "most actives" list (fallback: a fixed list of
   habitually high-volume tickers).
2. Flag large moves: |change vs prior close| >= MOVE_PCT, or a move of
   >= MOVE_SIGMA daily standard deviations.
3. For each flagged stock, decide whether the move is news-driven or
   automated / flow-driven (algorithmic execution, index or ETF flows,
   stop cascades, market-beta selling) from headline timing, move shape,
   volume profile and co-movement with SPY.
4. Rate it Strong Buy / Buy / Hold on a multi-factor composite of the kind
   fundamental hedge funds use: catalyst quality, momentum, valuation,
   analyst consensus, technicals and liquidity/risk.
5. Write reports/latest.md (full snapshot), append new or changed signals
   to reports/<date>.md, and pop a desktop notification for them.

Standard library only. Not investment advice.
"""

from __future__ import annotations

import argparse
import datetime as dt
import http.cookiejar
import json
import math
import os
import re
import shlex
import shutil
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from zoneinfo import ZoneInfo



class _USEastern(dt.tzinfo):
    """US Eastern time with current DST rules, for systems without a tz
    database (Windows without the tzdata package)."""

    def _dst_window(self, year: int) -> tuple[dt.datetime, dt.datetime]:
        mar = dt.datetime(year, 3, 8)   # second Sunday of March, 2am
        nov = dt.datetime(year, 11, 1)  # first Sunday of November, 2am
        return (mar + dt.timedelta(days=(6 - mar.weekday()) % 7, hours=2),
                nov + dt.timedelta(days=(6 - nov.weekday()) % 7, hours=2))

    def dst(self, d):
        start, end = self._dst_window(d.year)
        naive = d.replace(tzinfo=None)
        return dt.timedelta(hours=1 if start <= naive < end else 0)

    def utcoffset(self, d):
        return dt.timedelta(hours=-5) + self.dst(d)

    def tzname(self, d):
        return "EDT" if self.dst(d) else "EST"

    def fromutc(self, d):
        start, end = self._dst_window(d.year)
        naive = d.replace(tzinfo=None)
        summer = start + dt.timedelta(hours=5) <= naive < end + dt.timedelta(hours=4)
        return d + dt.timedelta(hours=-4 if summer else -5)


try:
    ET = ZoneInfo("America/New_York")
except Exception:
    ET = _USEastern()
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

TOP_N = int(os.environ.get("TOP_N", "25"))
MOVE_PCT = float(os.environ.get("MOVE_PCT", "3.0"))      # % vs prior close
MOVE_SIGMA = float(os.environ.get("MOVE_SIGMA", "2.0"))  # daily std devs
NEWS_LOOKBACK_H = 18                                     # covers overnight
REPORTS = os.environ.get(
    "REPORTS_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "reports"))
CACHE = os.path.join(REPORTS, ".cache")

FALLBACK_TICKERS = [
    "NVDA", "TSLA", "AAPL", "AMD", "PLTR", "AMZN", "MSFT", "META", "GOOGL",
    "INTC", "SOFI", "F", "BAC", "AAL", "NIO", "RIVN", "MARA", "SMCI", "MU",
    "PFE", "T", "WBD", "HOOD", "UBER", "AVGO",
]

# Headline keywords. "Strong" catalysts are the kind that reprice a stock on
# their own; the positive/negative lists set the direction of the news.
CATALYST = [
    "earnings", "results", "quarter", "guidance", "outlook", "forecast",
    "revenue", "eps", "upgrade", "downgrade", "price target", "fda",
    "approval", "trial", "acquire", "acquisition", "merger", "buyout",
    "deal", "sec ", "investigation", "probe", "lawsuit", "recall", "offering",
    "bankruptcy", "ceo", "resign", "layoff", "contract", "partnership",
    "tariff", "ban", "antitrust", "dividend", "buyback", "split", "halt",
    "short seller", "short report", "delist", "sanction", "subpoena",
]
STRONG_CATALYST = [
    "earnings", "guidance", "fda", "acquire", "acquisition", "merger",
    "buyout", "downgrade", "upgrade", "investigation", "probe", "bankruptcy",
    "offering", "recall", "short report", "short seller", "halt", "delist",
    "subpoena", "antitrust",
]
NEGATIVE = [
    "downgrade", "miss", "misses", "cut", "cuts", "lowers", "weak", "probe",
    "investigation", "lawsuit", "recall", "offering", "dilution", "bankruptcy",
    "resign", "layoff", "plunge", "tumble", "sink", "slump", "warn", "warning",
    "short seller", "short report", "halt", "delist", "subpoena", "ban",
    "sanction", "fraud", "decline", "disappoint",
]
POSITIVE = [
    "upgrade", "beat", "beats", "raise", "raises", "record", "approval",
    "approved", "buyback", "surge", "soar", "jump", "rally", "strong",
    "partnership", "contract", "wins", "acquire", "buyout", "outperform",
    "tops", "exceeds",
]


# ---------------------------------------------------------------- data layer

class FetchError(Exception):
    def __init__(self, code: int, url: str) -> None:
        super().__init__(f"HTTP {code} from {urllib.parse.urlsplit(url).netloc}")
        self.code = code


class Yahoo:
    """Minimal Yahoo Finance client (cookie + crumb aware).

    Yahoo often answers plain Python HTTP clients with 429 Too Many Requests
    regardless of volume, so requests go through the first transport that
    works: curl_cffi (if installed; impersonates Chrome), then urllib, then
    the system curl binary. Requests are spaced out and retried on 429."""

    GAP_S = 0.35   # minimum spacing between requests

    def __init__(self) -> None:
        self.jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.jar))
        self.crumb: str | None = None
        self.transport = "urllib"
        self.cffi = None
        try:
            from curl_cffi import requests as cffi_requests
            self.cffi = cffi_requests.Session(impersonate="chrome")
            self.transport = "curl_cffi"
        except Exception:
            pass
        self.curl_jar = os.path.join(CACHE, "cookies.txt")
        self._last = 0.0

    def _fetch(self, url: str, timeout: int) -> bytes:
        wait = self.GAP_S - (time.time() - self._last)
        if wait > 0:
            time.sleep(wait)
        self._last = time.time()
        if self.transport == "curl_cffi":
            r = self.cffi.get(url, timeout=timeout)
            if r.status_code >= 400:
                raise FetchError(r.status_code, url)
            return r.content
        if self.transport == "curl":
            os.makedirs(CACHE, exist_ok=True)
            p = subprocess.run(
                ["curl", "-sS", "-L", "--compressed", "-m", str(timeout),
                 "-A", UA, "-H", "Accept: */*", "-b", self.curl_jar,
                 "-c", self.curl_jar, "-w", "\n%{http_code}", url],
                capture_output=True, timeout=timeout + 5)
            body, _, code = p.stdout.rpartition(b"\n")
            status = int(code or 0)
            if p.returncode or status >= 400 or status == 0:
                raise FetchError(status, url)
            return body
        req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                   "Accept": "*/*"})
        try:
            with self.opener.open(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            raise FetchError(e.code, url) from None

    def _get(self, url: str, timeout: int = 15) -> bytes:
        for attempt in range(4):
            try:
                return self._fetch(url, timeout)
            except FetchError as e:
                if e.code not in (429, 403, 999) or attempt == 3:
                    raise
                # Blocked: fall back to the system curl binary once, then
                # back off and alternate Yahoo's two API hosts.
                if self.transport == "urllib" and shutil.which("curl"):
                    self.transport = "curl"
                    url = self._reauth(url, timeout)
                    continue
                time.sleep(2 * (attempt + 1))
                url = (url.replace("//query1.", "//query2.")
                       if "//query1." in url
                       else url.replace("//query2.", "//query1."))
        raise AssertionError("unreachable")

    def _reauth(self, url: str, timeout: int) -> str:
        """After switching transport, cookies and crumb must be re-issued."""
        if "getcrumb" in url:
            try:
                self._fetch("https://fc.yahoo.com", timeout)
            except FetchError:
                pass  # 404 is expected; it still sets the cookie
            return url
        if "crumb=" in url:
            self.crumb = None
            url = re.sub(r"[&?]crumb=[^&]*", "", url)
            self._ensure_crumb()
            if self.crumb:
                sep = "&" if "?" in url else "?"
                url += f"{sep}crumb={urllib.parse.quote(self.crumb)}"
        else:
            self.crumb = None
        return url

    def _json(self, url: str, crumb: bool = False) -> dict:
        if crumb:
            self._ensure_crumb()
            if self.crumb:
                sep = "&" if "?" in url else "?"
                url += f"{sep}crumb={urllib.parse.quote(self.crumb)}"
        return json.loads(self._get(url))

    def _ensure_crumb(self) -> None:
        if self.crumb is not None:
            return
        self.crumb = ""
        try:
            try:
                self._get("https://fc.yahoo.com")
            except Exception:
                pass  # 404 is expected; it still sets the cookie
            self.crumb = self._get(
                "https://query1.finance.yahoo.com/v1/test/getcrumb").decode()
        except Exception:
            self.crumb = ""

    def most_active(self, n: int) -> list[dict]:
        url = ("https://query1.finance.yahoo.com/v1/finance/screener/"
               f"predefined/saved?scrIds=most_actives&count={n}")
        data = self._json(url, crumb=True)
        return data["finance"]["result"][0]["quotes"]

    def quotes(self, symbols: list[str]) -> list[dict]:
        url = ("https://query1.finance.yahoo.com/v7/finance/quote?symbols="
               + urllib.parse.quote(",".join(symbols)))
        return self._json(url, crumb=True)["quoteResponse"]["result"]

    def chart(self, symbol: str, rng: str, interval: str) -> dict:
        url = (f"https://query1.finance.yahoo.com/v8/finance/chart/"
               f"{urllib.parse.quote(symbol)}?range={rng}&interval={interval}"
               "&includePrePost=false")
        return self._json(url)["chart"]["result"][0]

    def news(self, symbol: str) -> list[dict]:
        """Headlines as {title, publisher, ts (epoch s), link}."""
        out: list[dict] = []
        try:
            url = ("https://query1.finance.yahoo.com/v1/finance/search?q="
                   f"{urllib.parse.quote(symbol)}&quotesCount=0&newsCount=15")
            for n in self._json(url).get("news", []):
                out.append({"title": n.get("title", ""),
                            "publisher": n.get("publisher", ""),
                            "ts": n.get("providerPublishTime", 0),
                            "link": n.get("link", "")})
        except Exception:
            pass
        try:
            out.extend(google_news(self, symbol))
        except Exception:
            pass
        seen, uniq = set(), []
        for n in sorted(out, key=lambda n: -n["ts"]):
            key = re.sub(r"\W+", "", n["title"].lower())[:60]
            if key and key not in seen:
                seen.add(key)
                uniq.append(n)
        return uniq


def google_news(y: Yahoo, symbol: str) -> list[dict]:
    import email.utils
    import xml.etree.ElementTree as ET_xml
    q = urllib.parse.quote(f"{symbol} stock when:1d")
    raw = y._get(f"https://news.google.com/rss/search?q={q}"
                 "&hl=en-US&gl=US&ceid=US:en")
    out = []
    for item in ET_xml.fromstring(raw).iter("item"):
        pub = item.findtext("pubDate") or ""
        try:
            ts = int(email.utils.parsedate_to_datetime(pub).timestamp())
        except Exception:
            continue
        src = item.find("source")
        out.append({"title": item.findtext("title") or "",
                    "publisher": src.text if src is not None else "",
                    "ts": ts, "link": item.findtext("link") or ""})
    return out


@dataclass
class Bars:
    ts: list[int]
    open: list[float]
    high: list[float]
    low: list[float]
    close: list[float]
    volume: list[float]

    @classmethod
    def from_chart(cls, c: dict) -> "Bars":
        q = c["indicators"]["quote"][0]
        rows = [r for r in zip(c.get("timestamp", []), q["open"], q["high"],
                               q["low"], q["close"], q["volume"])
                if None not in r]
        cols = list(zip(*rows)) if rows else [[]] * 6
        return cls(*[list(x) for x in cols])


# ------------------------------------------------------------ move analysis

def pct(a: float, b: float) -> float:
    return (a / b - 1.0) * 100.0 if b else 0.0


def returns(xs: list[float]) -> list[float]:
    return [xs[i] / xs[i - 1] - 1 for i in range(1, len(xs)) if xs[i - 1]]


def daily_sigma_pct(daily: Bars, lookback: int = 20) -> float:
    r = returns(daily.close[-(lookback + 1):])
    return statistics.pstdev(r) * 100 if len(r) >= 5 else 0.0


def beta_and_corr(stock: Bars, mkt: Bars) -> tuple[float, float]:
    m = dict(zip(mkt.ts, mkt.close))
    pairs = [(s, m[t]) for t, s in zip(stock.ts, stock.close) if t in m]
    if len(pairs) < 8:
        return 1.0, 0.0
    rs = returns([p[0] for p in pairs])
    rm = returns([p[1] for p in pairs])
    var_m = statistics.pvariance(rm)
    if var_m == 0:
        return 1.0, 0.0
    mean_s, mean_m = statistics.fmean(rs), statistics.fmean(rm)
    cov = sum((a - mean_s) * (b - mean_m) for a, b in zip(rs, rm)) / len(rs)
    sd_s = statistics.pstdev(rs)
    corr = cov / (sd_s * math.sqrt(var_m)) if sd_s else 0.0
    return cov / var_m, corr


def third_friday(d: dt.date) -> dt.date:
    first = d.replace(day=1)
    return first + dt.timedelta(days=(4 - first.weekday()) % 7 + 14)


@dataclass
class Move:
    symbol: str
    name: str
    price: float
    prev_close: float
    move_pct: float
    move_sigma: float
    rel_volume: float
    gap_share: float           # share of the move that came at the open
    max_bar_share: float       # largest single 5m bar / total move
    dir_bar_frac: float        # fraction of bars in the move's direction
    bar_cv: float              # dispersion of in-direction bar sizes
    vol_top3_share: float      # volume in the 3 busiest bars / total
    retrace: float             # share of the extreme move given back
    market_share: float        # part of the move explained by beta * SPY
    corr_spy: float
    beta: float
    close_window_share: float  # share of move made after 15:45 ET
    biggest_bar_ts: int
    session_open_ts: int
    special_day: str = ""
    headlines: list[dict] = field(default_factory=list)


def analyse_move(symbol: str, name: str, intraday: Bars, daily: Bars,
                 spy: Bars, prev_close: float, avg_volume: float,
                 now: dt.datetime) -> Move | None:
    if len(intraday.close) < 3 or not prev_close:
        return None
    last = intraday.close[-1]
    total = last - prev_close
    move_pct = pct(last, prev_close)
    sigma = daily_sigma_pct(daily)
    move_sigma = abs(move_pct) / sigma if sigma else 0.0
    sign = 1 if total >= 0 else -1

    # Per-bar price changes, with the opening gap treated as bar 0.
    steps = [intraday.open[0] - prev_close]
    steps += [intraday.close[0] - intraday.open[0]]
    steps += [intraday.close[i] - intraday.close[i - 1]
              for i in range(1, len(intraday.close))]
    denom = abs(total) or 1e-9
    gap_share = max(0.0, sign * steps[0] / denom)
    intraday_steps = steps[1:]
    max_bar_share = max(sign * s for s in steps) / denom
    in_dir = [abs(s) for s in intraday_steps if sign * s > 0]
    dir_bar_frac = len(in_dir) / len(intraday_steps)
    bar_cv = (statistics.pstdev(in_dir) / statistics.fmean(in_dir)
              if len(in_dir) >= 3 else 9.9)
    big_i = max(range(len(steps)), key=lambda i: sign * steps[i])
    biggest_bar_ts = intraday.ts[max(0, big_i - 1)]

    vols = intraday.volume
    tot_vol = sum(vols) or 1
    vol_top3_share = sum(sorted(vols, reverse=True)[:3]) / tot_vol
    # Relative volume vs the same fraction of an average full day.
    minutes = max(5, (intraday.ts[-1] - intraday.ts[0]) / 60 + 5)
    rel_volume = (tot_vol / (avg_volume * minutes / 390)
                  if avg_volume else 0.0)

    extreme = (max(intraday.high) if sign > 0 else min(intraday.low))
    ext_move = abs(extreme - prev_close) or 1e-9
    retrace = abs(extreme - last) / ext_move

    beta, corr = beta_and_corr(intraday, spy)
    spy_move = pct(spy.close[-1], spy.open[0]) if spy.close else 0.0
    explained = beta * spy_move if corr > 0.3 else 0.0
    market_share = (max(0.0, min(1.0, explained / move_pct))
                    if move_pct else 0.0)

    cutoff = now.astimezone(ET).replace(hour=15, minute=45, second=0)
    after = [c for t, c in zip(intraday.ts, intraday.close)
             if t >= cutoff.timestamp()]
    close_window_share = 0.0
    if after:
        before_idx = len(intraday.close) - len(after) - 1
        base = intraday.close[before_idx] if before_idx >= 0 else prev_close
        close_window_share = max(0.0, sign * (last - base) / denom)

    today = now.astimezone(ET).date()
    special = ""
    if today == third_friday(today):
        special = ("quarterly index rebalance / triple witching"
                   if today.month in (3, 6, 9, 12) else "monthly options expiry")

    return Move(symbol, name, last, prev_close, move_pct, move_sigma,
                rel_volume, gap_share, max_bar_share, dir_bar_frac, bar_cv,
                vol_top3_share, retrace, market_share, corr, beta,
                close_window_share, biggest_bar_ts, intraday.ts[0], special)


def has(words: list[str], text: str) -> list[str]:
    t = f" {text.lower()} "
    return [w for w in words if re.search(rf"\b{re.escape(w.strip())}\b", t)]


@dataclass
class Verdict:
    label: str            # News-driven | Automated/flow-driven | Mixed
    confidence: int       # 0-100
    news_score: int
    flow_score: int
    news_tone: str        # positive | negative | neutral | none
    reasons: list[str]
    catalysts: list[dict]


def classify(m: Move, now: dt.datetime) -> Verdict:
    since = now.timestamp() - NEWS_LOOKBACK_H * 3600
    fresh = [h for h in m.headlines if h["ts"] >= since]
    cats = [h for h in fresh if has(CATALYST, h["title"])]
    strong = [h for h in cats if has(STRONG_CATALYST, h["title"])]
    pos = sum(len(has(POSITIVE, h["title"])) for h in cats)
    neg = sum(len(has(NEGATIVE, h["title"])) for h in cats)
    tone = ("none" if not cats else "positive" if pos > neg
            else "negative" if neg > pos else "neutral")
    aligned = [h for h in cats
               if abs(h["ts"] - m.biggest_bar_ts) <= 45 * 60
               or (m.gap_share >= 0.5 and h["ts"] <= m.session_open_ts)]
    down = m.move_pct < 0

    news, flow, why = 0, 0, []
    if cats:
        news += 35
        why.append(f"{len(cats)} catalyst headline(s) in last "
                   f"{NEWS_LOOKBACK_H}h")
    if strong:
        news += 15
        why.append("hard catalyst: " + ", ".join(
            sorted({k for h in strong for k in has(STRONG_CATALYST,
                                                   h["title"])})))
    if aligned:
        news += 20
        why.append("headline timing lines up with the move")
    if tone != "none" and (tone == "negative") == down and tone != "neutral":
        news += 5
    if m.gap_share >= 0.5:
        news += 10
        why.append(f"{m.gap_share:.0%} of move was the opening gap")
    if m.max_bar_share >= 0.35:
        news += 10
        why.append(f"single 5m bar made {m.max_bar_share:.0%} of the move")
    if m.market_share <= 0.3:
        news += 10

    if not cats:
        flow += 25
        why.append("no catalyst headlines found")
    if m.market_share >= 0.5:
        flow += 20
        why.append(f"{m.market_share:.0%} of move explained by SPY beta "
                   f"(beta {m.beta:.2f}, corr {m.corr_spy:.2f})")
    if m.dir_bar_frac >= 0.6 and m.bar_cv < 0.8:
        flow += 15
        why.append("steady, evenly sized bars (execution-algo footprint)")
    if m.vol_top3_share < 0.25 and m.rel_volume >= 1.3:
        flow += 15
        why.append("heavy but evenly spread volume (TWAP/VWAP-style)")
    if m.retrace >= 0.4:
        flow += 10
        why.append(f"{m.retrace:.0%} of the extreme retraced "
                   "(stop cascade / liquidation)")
    if m.close_window_share >= 0.5:
        flow += 10
        why.append("move concentrated after 15:45 ET (MOC imbalance)")
    if m.special_day:
        flow += 10
        why.append(m.special_day)
    if m.gap_share < 0.2:
        flow += 5

    news, flow = min(news, 100), min(flow, 100)
    if news >= flow + 15:
        label = "News-driven"
    elif flow >= news + 15:
        label = ("Automated/flow-driven selling" if down
                 else "Automated/flow-driven buying")
    else:
        label = "Mixed / unclear"
    return Verdict(label, min(100, abs(news - flow) * 2), news, flow, tone,
                   why, cats[:3])


# ------------------------------------------------------------------ rating

@dataclass
class Rating:
    rating: str
    score: float
    factors: dict[str, float]


def rsi(closes: list[float], n: int = 14) -> float:
    if len(closes) <= n:
        return 50.0
    d = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    gain = sum(max(x, 0) for x in d[:n]) / n
    loss = sum(max(-x, 0) for x in d[:n]) / n
    for x in d[n:]:
        gain = (gain * (n - 1) + max(x, 0)) / n
        loss = (loss * (n - 1) + max(-x, 0)) / n
    return 100.0 if loss == 0 else 100 - 100 / (1 + gain / loss)


def clamp(x: float, lo: float = 0, hi: float = 100) -> float:
    return max(lo, min(hi, x))


def rate(m: Move, v: Verdict, q: dict, daily: Bars) -> Rating:
    down = m.move_pct < 0
    flow = v.label.startswith("Automated")

    # 1. Catalyst quality: forced/flow selling in a sound name is a classic
    #    dislocation to buy; bad fundamental news is not.
    if flow:
        catalyst = 80 if down else 45
    elif v.label == "News-driven":
        if down:
            catalyst = 20 if v.news_tone == "negative" else 45
        else:
            catalyst = 75 if v.news_tone == "positive" else 55
    else:
        catalyst = 50

    # 2. Momentum / trend: 12-1 month return and moving averages.
    c = daily.close
    price = m.price
    ma50 = q.get("fiftyDayAverage") or (statistics.fmean(c[-50:])
                                        if len(c) >= 50 else price)
    ma200 = q.get("twoHundredDayAverage") or (statistics.fmean(c[-200:])
                                              if len(c) >= 200 else ma50)
    mom = 50.0
    mom += 15 if price > ma200 else -15
    mom += 10 if price > ma50 else -10
    mom += 10 if ma50 > ma200 else -10
    if len(c) >= 150:
        r = pct(c[-22], c[max(0, len(c) - 252)]) / 100
        mom += clamp(r / 0.3 * 15, -15, 15)
    hi52 = q.get("fiftyTwoWeekHigh") or (max(c) if c else price)
    if hi52 and price >= 0.9 * hi52:
        mom += 5
    momentum = clamp(mom)

    # 3. Valuation: forward P/E level plus implied earnings growth (PEG).
    fpe, tpe = q.get("forwardPE"), q.get("trailingPE")
    if fpe is None and tpe is None:
        valuation = 50.0
    elif fpe is not None and fpe <= 0:
        valuation = 25.0
    else:
        pe = fpe or tpe
        valuation = (75 if pe < 12 else 65 if pe < 18 else 55 if pe < 25
                     else 45 if pe < 35 else 35 if pe < 50 else 25)
        if fpe and tpe and tpe > 0:
            g = tpe / fpe - 1
            if g > 0.1 and fpe / (g * 100) < 1:
                valuation += 10
            elif g < 0:
                valuation -= 10
    valuation = clamp(valuation)

    # 4. Street consensus, e.g. "1.8 - Buy" (1 = strong buy, 5 = sell).
    analyst = 50.0
    try:
        a = float(str(q.get("averageAnalystRating", "")).split("-")[0])
        analyst = clamp((5 - a) / 4 * 100)
    except ValueError:
        pass

    # 5. Technicals / mean reversion.
    r14 = rsi(c + [price]) if c else 50.0
    tech = (80 if r14 < 30 else 65 if r14 < 40 else 30 if r14 > 70
            else 40 if r14 > 60 else 50)
    if flow and down and m.move_sigma >= 2.5:
        tech += 10
    technical = clamp(tech)

    # 6. Liquidity / risk.
    cap = q.get("marketCap") or 0
    risk = 80 if cap >= 2e11 else 65 if cap >= 1e10 else 50 if cap >= 2e9 \
        else 30
    ann_vol = daily_sigma_pct(daily, 60) * math.sqrt(252)
    risk -= 20 if ann_vol > 80 else 10 if ann_vol > 50 else 0
    risk = clamp(risk)

    f = {"catalyst": catalyst, "momentum": momentum, "valuation": valuation,
         "analyst": analyst, "technical": technical, "risk": risk}
    w = {"catalyst": .25, "momentum": .20, "valuation": .20,
         "analyst": .15, "technical": .10, "risk": .10}
    score = sum(f[k] * w[k] for k in f)
    bad_news = v.label == "News-driven" and down and v.news_tone == "negative"
    if score >= 68 and catalyst >= 60 and not bad_news:
        label = "Strong Buy"
    elif score >= 56 and not bad_news:
        label = "Buy"
    else:
        label = "Hold"
    return Rating(label, round(score, 1), {k: round(x) for k, x in f.items()})


# ------------------------------------------------------------------- runner

def in_session_window(now: dt.datetime) -> bool:
    et = now.astimezone(ET)
    return (et.weekday() < 5
            and dt.time(9, 35) <= et.time() <= dt.time(16, 5))


def cached_daily(y: Yahoo, sym: str, now: dt.datetime) -> dict:
    """1y of daily bars, fetched once per symbol per day (they only change
    at the close), which cuts each scan's requests by a third."""
    path = os.path.join(CACHE, f"daily-{sym}-{now.astimezone(ET):%Y%m%d}"
                               ".json")
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        pass
    c = y.chart(sym, "1y", "1d")
    try:
        os.makedirs(CACHE, exist_ok=True)
        for old in os.listdir(CACHE):
            if old.startswith(f"daily-{sym}-"):
                os.remove(os.path.join(CACHE, old))
        with open(path, "w") as f:
            json.dump(c, f)
    except OSError:
        pass
    return c


def diagnose() -> None:
    """Check each data source and transport; prints one line per check."""
    y = Yahoo()
    checks = [
        ("price chart", "https://query1.finance.yahoo.com/v8/finance/chart/"
                        "SPY?range=1d&interval=5m"),
        ("cookie", "https://fc.yahoo.com"),
        ("crumb", "https://query1.finance.yahoo.com/v1/test/getcrumb"),
        ("news", "https://query1.finance.yahoo.com/v1/finance/search?q=AAPL"
                 "&quotesCount=0&newsCount=3"),
        ("google news", "https://news.google.com/rss/search?q=AAPL"),
    ]
    transports = (["curl_cffi"] if y.cffi else []) + ["urllib"] + (
        ["curl"] if shutil.which("curl") else [])
    for t in transports:
        y.transport = t
        for name, url in checks:
            try:
                n = len(y._fetch(url, 15))
                print(f"{t:9} {name:12} OK ({n} bytes)")
            except FetchError as e:
                print(f"{t:9} {name:12} {e}")
            except Exception as e:
                print(f"{t:9} {name:12} error: {e}")
    try:
        y.transport = transports[0]
        y.crumb = None
        print(f"most actives: {len(y.most_active(5))} rows")
    except Exception as e:
        print(f"most actives: failed ({e})")


def market_open(now: dt.datetime, spy: Bars) -> bool:
    if not in_session_window(now):
        return False
    # Holidays: no fresh SPY bar today.
    return bool(spy.ts) and now.timestamp() - spy.ts[-1] < 20 * 60


def scan(now: dt.datetime, force: bool = False) -> tuple[str, list[dict]]:
    y = Yahoo()
    spy = Bars.from_chart(y.chart("SPY", "1d", "5m"))
    if not force and not market_open(now, spy):
        return "", []

    try:
        universe = y.most_active(TOP_N)
        source = "Yahoo most actives"
    except Exception:
        universe = []
    if not universe:
        try:
            universe = y.quotes(FALLBACK_TICKERS[:TOP_N])
        except Exception:
            universe = [{"symbol": s} for s in FALLBACK_TICKERS[:TOP_N]]
        source = "fallback ticker list"

    results: list[dict] = []
    for q in universe:
        sym = q["symbol"]
        try:
            ic = y.chart(sym, "1d", "5m")
            intraday = Bars.from_chart(ic)
            daily = Bars.from_chart(cached_daily(y, sym, now))
            # Drop today's (partial) daily bar so it doesn't skew stats.
            if daily.ts and dt.datetime.fromtimestamp(
                    daily.ts[-1], ET).date() == now.astimezone(ET).date():
                daily = Bars(*[col[:-1] for col in (
                    daily.ts, daily.open, daily.high, daily.low,
                    daily.close, daily.volume)])
            prev = (q.get("regularMarketPreviousClose")
                    or ic["meta"].get("chartPreviousClose")
                    or (daily.close[-1] if daily.close else 0))
            avg_vol = (q.get("averageDailyVolume3Month")
                       or (statistics.fmean(daily.volume[-60:])
                           if daily.volume else 0))
            m = analyse_move(sym, q.get("shortName", sym), intraday, daily,
                             spy, prev, avg_vol, now)
            if not m or not (abs(m.move_pct) >= MOVE_PCT
                             or m.move_sigma >= MOVE_SIGMA):
                continue
            m.headlines = y.news(sym)
            v = classify(m, now)
            r = rate(m, v, q, daily)
            results.append({"move": m, "verdict": v, "rating": r})
        except Exception as e:  # one bad ticker shouldn't kill the run
            print(f"warn: {sym}: {e}", file=sys.stderr)

    results.sort(key=lambda x: -abs(x["move"].move_pct))
    spy_move = pct(spy.close[-1], spy.open[0]) if spy.close else 0.0
    header = (f"Universe: top {len(universe)} by volume ({source}). "
              f"SPY {spy_move:+.2f}% today. Threshold: ≥{MOVE_PCT:g}% "
              f"or ≥{MOVE_SIGMA:g}σ.")
    return render(now, header, results), results


def render(now: dt.datetime, header: str, results: list[dict]) -> str:
    et = now.astimezone(ET)
    out = [f"## Large moves — {et:%Y-%m-%d %H:%M} ET", header, ""]
    if not results:
        out.append("No large moves right now.")
        return "\n".join(out)
    out += ["| Ticker | Move | σ | RelVol | Driver | Conf. | Rating | Score |",
            "|---|---|---|---|---|---|---|---|"]
    for x in results:
        m, v, r = x["move"], x["verdict"], x["rating"]
        out.append(f"| **{m.symbol}** | {m.move_pct:+.2f}% | "
                   f"{m.move_sigma:.1f} | {m.rel_volume:.1f}x | {v.label} | "
                   f"{v.confidence} | **{r.rating}** | {r.score} |")
    for x in results:
        m, v, r = x["move"], x["verdict"], x["rating"]
        out += ["", f"### {m.symbol} — {m.name} · ${m.price:,.2f} "
                f"({m.move_pct:+.2f}%)",
                f"**{v.label}** (news {v.news_score} vs flow {v.flow_score}, "
                f"headline tone: {v.news_tone}) → **{r.rating}** ({r.score})",
                "- Evidence: " + ("; ".join(v.reasons) or "—"),
                "- Factors (0-100): " + ", ".join(
                    f"{k} {s}" for k, s in r.factors.items())]
        for h in v.catalysts:
            t = dt.datetime.fromtimestamp(h["ts"], ET)
            out.append(f"- {t:%m-%d %H:%M} [{h['title']}]({h['link']}) "
                       f"— {h['publisher']}")
    out += ["", "_Automated screen, not investment advice._"]
    return "\n".join(out)


# ------------------------------------------------------------ alert output

def load_state(path: str) -> dict:
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def new_signals(results: list[dict], state: dict, today: str) -> list[dict]:
    """Signals not yet alerted today, or whose driver/rating changed or
    whose move widened by 2+ points since the last alert."""
    if state.get("date") != today:
        state.clear()
        state["date"] = today
    seen = state.setdefault("seen", {})
    fresh = []
    for x in results:
        m, v, r = x["move"], x["verdict"], x["rating"]
        prev = seen.get(m.symbol)
        if (prev is None or prev["label"] != v.label
                or prev["rating"] != r.rating
                or abs(m.move_pct) - abs(prev["move"]) >= 2):
            fresh.append(x)
            seen[m.symbol] = {"label": v.label, "rating": r.rating,
                              "move": m.move_pct}
    return fresh


def notify(title: str, body: str) -> None:
    """Best-effort desktop notification on macOS, Linux or Windows."""
    try:
        if sys.platform == "darwin":
            script = (f"display notification {json.dumps(body)} "
                      f"with title {json.dumps(title)}")
            subprocess.run(["osascript", "-e", script], timeout=10)
        elif sys.platform.startswith("win"):
            ps = (
                "Add-Type -AssemblyName System.Windows.Forms;"
                "$n=New-Object System.Windows.Forms.NotifyIcon;"
                "$n.Icon=[System.Drawing.SystemIcons]::Information;"
                "$n.Visible=$true;"
                f"$n.ShowBalloonTip(10000,{ps_quote(title)},{ps_quote(body)},"
                "'Info');Start-Sleep 11;$n.Dispose()")
            subprocess.Popen(["powershell", "-NoProfile", "-Command", ps],
                             creationflags=0x08000000)  # no console window
        elif shutil.which("notify-send"):
            subprocess.run(["notify-send", title, body], timeout=10)
    except Exception as e:
        print(f"warn: notification failed: {e}", file=sys.stderr)


def ps_quote(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def one_liner(x: dict) -> str:
    m, v, r = x["move"], x["verdict"], x["rating"]
    driver = "news" if v.label == "News-driven" else (
        "automated" if v.label.startswith("Automated") else "mixed")
    return f"{m.symbol} {m.move_pct:+.1f}% ({driver}) → {r.rating}"


def run_once(force: bool, alert: bool) -> None:
    now = dt.datetime.now(dt.timezone.utc)
    if not force and not in_session_window(now):
        return  # cheap exit, no network, for scheduler ticks off-hours
    report, results = scan(now, force)
    if not report:
        print("Market closed — nothing to do.")
        return
    print(report, flush=True)
    os.makedirs(REPORTS, exist_ok=True)
    with open(os.path.join(REPORTS, "latest.md"), "w") as f:
        f.write(report + "\n")

    state_path = os.path.join(REPORTS, ".state.json")
    state = load_state(state_path)
    today = str(now.astimezone(ET).date())
    fresh = new_signals(results, state, today)
    with open(state_path, "w") as f:
        json.dump(state, f)
    if fresh:
        with open(os.path.join(REPORTS, f"{today}.md"), "a") as f:
            f.write(render(now, f"{len(fresh)} new or changed signal(s).",
                           fresh) + "\n\n")
        if alert:
            notify(f"Market moves: {len(fresh)} new signal(s)",
                   "\n".join(one_liner(x) for x in fresh[:5]))


# --------------------------------------------------------------- scheduling

TASK = "com.tempore.market-moves"
PLIST = os.path.expanduser(f"~/Library/LaunchAgents/{TASK}.plist")
CRON_TAG = "# market-moves-scanner"


def install() -> None:
    py, script = sys.executable, os.path.abspath(__file__)
    log = os.path.join(REPORTS, "scanner.log")
    os.makedirs(REPORTS, exist_ok=True)
    if sys.platform == "darwin":
        os.makedirs(os.path.dirname(PLIST), exist_ok=True)
        with open(PLIST, "w") as f:
            f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>{TASK}</string>
  <key>ProgramArguments</key>
  <array><string>{py}</string><string>{script}</string></array>
  <key>StartInterval</key><integer>300</integer>
  <key>StandardOutPath</key><string>{log}</string>
  <key>StandardErrorPath</key><string>{log}</string>
</dict></plist>
""")
        subprocess.run(["launchctl", "unload", PLIST], capture_output=True)
        subprocess.run(["launchctl", "load", PLIST], check=True)
        print(f"Installed launchd agent {PLIST}")
    elif sys.platform.startswith("win"):
        pyw = os.path.join(os.path.dirname(py), "pythonw.exe")
        exe = pyw if os.path.exists(pyw) else py
        subprocess.run(["schtasks", "/Create", "/F", "/SC", "MINUTE",
                        "/MO", "5", "/TN", "MarketMoveScanner",
                        "/TR", f'"{exe}" "{script}"'], check=True)
        print("Installed Task Scheduler task MarketMoveScanner")
    else:
        line = (f"*/5 * * * 1-5 {shlex.quote(py)} {shlex.quote(script)} "
                f">> {shlex.quote(log)} 2>&1 {CRON_TAG}")
        cur = subprocess.run(["crontab", "-l"], capture_output=True,
                             text=True).stdout
        keep = [ln for ln in cur.splitlines() if CRON_TAG not in ln]
        subprocess.run(["crontab", "-"], input="\n".join(keep + [line])
                       + "\n", text=True, check=True)
        print("Installed crontab entry:\n  " + line)
    print(f"Reports: {REPORTS}")


def uninstall() -> None:
    if sys.platform == "darwin":
        subprocess.run(["launchctl", "unload", PLIST], capture_output=True)
        if os.path.exists(PLIST):
            os.remove(PLIST)
    elif sys.platform.startswith("win"):
        subprocess.run(["schtasks", "/Delete", "/F", "/TN",
                        "MarketMoveScanner"])
    else:
        cur = subprocess.run(["crontab", "-l"], capture_output=True,
                             text=True).stdout
        keep = [ln for ln in cur.splitlines() if CRON_TAG not in ln]
        subprocess.run(["crontab", "-"], input="\n".join(keep) + "\n",
                       text=True, check=True)
    print("Schedule removed.")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--force", action="store_true",
                    help="run even when the market is closed")
    ap.add_argument("--no-alert", action="store_true",
                    help="skip desktop notifications")
    ap.add_argument("--every", type=float, metavar="MIN",
                    help="stay running and scan every MIN minutes")
    ap.add_argument("--install", action="store_true",
                    help="schedule a scan every 5 minutes on this computer")
    ap.add_argument("--uninstall", action="store_true",
                    help="remove the schedule")
    ap.add_argument("--diagnose", action="store_true",
                    help="test the data sources and print what works")
    args = ap.parse_args()

    if args.diagnose:
        diagnose()
        return 0

    if args.install:
        install()
        return 0
    if args.uninstall:
        uninstall()
        return 0
    while True:
        try:
            run_once(args.force, not args.no_alert)
        except Exception as e:  # network down, Yahoo changed, etc.
            stamp = f"{dt.datetime.now(ET):%Y-%m-%d %H:%M}"
            print(f"{stamp} error: {e}", file=sys.stderr, flush=True)
            if not args.every:
                return 1
        if not args.every:
            return 0
        period = args.every * 60
        time.sleep(period - time.time() % period + 2)  # align to the clock


if __name__ == "__main__":
    sys.exit(main())
