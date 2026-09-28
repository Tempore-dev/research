#!/usr/bin/env python3
"""Large-move scanner for the most traded US stocks.

Runs on your own computer, every 5 minutes during US market hours
(install the schedule with `python3 scanner.py --install`). Each run:

1. Pull the most traded stocks from Alpaca's market data API (fallback:
   a fixed list of habitually high-volume tickers).
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

Data: Alpaca (free account; keys via `--setup`) for the most-actives list,
5-minute and daily bars and news; Google News for extra headlines; Yahoo
Finance, best effort, for P/E, analyst rating and market cap.

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

CONFIG = os.path.join(os.path.expanduser("~"), ".config",
                      "market-moves-scanner", "alpaca.json")


class FetchError(Exception):
    def __init__(self, code: int, url: str, detail: str = "") -> None:
        host = urllib.parse.urlsplit(url).netloc
        super().__init__(f"HTTP {code} from {host}"
                         + (f": {detail[:200]}" if detail else ""))
        self.code = code


def http_get(url: str, headers: dict | None = None, timeout: int = 20,
             opener=None) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "*/*",
                                               **(headers or {})})
    try:
        fetch = opener.open if opener else urllib.request.urlopen
        with fetch(req, timeout=timeout) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace") if e.fp else ""
        raise FetchError(e.code, url, detail) from None


def parse_ts(s: str) -> int:
    """RFC 3339 (Alpaca's format, sometimes with nanoseconds) -> epoch s."""
    s = re.sub(r"\.\d+", "", s).replace("Z", "+00:00")
    return int(dt.datetime.fromisoformat(s).timestamp())


def load_keys() -> tuple[str, str, str]:
    """Alpaca key id, secret and data feed, from the environment or the
    config file written by --setup (schedulers don't see shell variables)."""
    cfg: dict = {}
    try:
        with open(CONFIG) as f:
            cfg = json.load(f)
    except (OSError, ValueError):
        pass
    key = (os.environ.get("ALPACA_API_KEY_ID")
           or os.environ.get("APCA_API_KEY_ID") or cfg.get("key_id", ""))
    secret = (os.environ.get("ALPACA_API_SECRET_KEY")
              or os.environ.get("APCA_API_SECRET_KEY")
              or cfg.get("secret_key", ""))
    feed = os.environ.get("ALPACA_FEED") or cfg.get("feed", "iex")
    return key, secret, feed


class Alpaca:
    """Alpaca market data API (https://data.alpaca.markets).

    The free plan gives real-time bars from the IEX exchange (feed "iex"),
    which carries a few percent of US volume; relative-volume figures stay
    consistent because every bar comes from the same feed. "delayed_sip"
    (free, 15 min delay) or "sip" (paid) use the full consolidated tape."""

    BASE = "https://data.alpaca.markets"

    def __init__(self, key: str, secret: str, feed: str = "iex") -> None:
        if not key or not secret:
            raise SystemExit(
                "No Alpaca API keys found. Run: python3 scanner.py --setup")
        self.headers = {"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret}
        self.feed = feed

    @classmethod
    def from_config(cls) -> "Alpaca":
        return cls(*load_keys())

    def _get(self, path: str, params: dict) -> dict:
        q = urllib.parse.urlencode({k: v for k, v in params.items()
                                    if v is not None})
        url = f"{self.BASE}{path}?{q}"
        for attempt in range(3):
            try:
                return json.loads(http_get(url, self.headers))
            except FetchError as e:
                if e.code != 429 or attempt == 2:
                    raise
                time.sleep(3 * (attempt + 1))  # free plan: 200 requests/min
        raise AssertionError("unreachable")

    def most_active(self, n: int) -> list[str]:
        data = self._get("/v1beta1/screener/stocks/most-actives",
                         {"by": "volume", "top": n})
        return [x["symbol"] for x in data.get("most_actives", [])]

    def bars(self, symbols: list[str], timeframe: str, start: dt.datetime,
             end: dt.datetime | None = None,
             adjustment: str = "raw") -> dict[str, list[dict]]:
        out: dict[str, list[dict]] = {}
        params = {"symbols": ",".join(symbols), "timeframe": timeframe,
                  "start": start.astimezone(dt.timezone.utc).strftime(
                      "%Y-%m-%dT%H:%M:%SZ"),
                  "end": end.astimezone(dt.timezone.utc).strftime(
                      "%Y-%m-%dT%H:%M:%SZ") if end else None,
                  "limit": 10000, "adjustment": adjustment,
                  "feed": self.feed, "sort": "asc"}
        while True:
            data = self._get("/v2/stocks/bars", params)
            for sym, rows in (data.get("bars") or {}).items():
                out.setdefault(sym, []).extend(rows)
            params["page_token"] = data.get("next_page_token")
            if not params["page_token"]:
                return out

    def news(self, symbols: list[str], since: dt.datetime,
             pages: int = 4) -> dict[str, list[dict]]:
        """Headlines per symbol as {title, publisher, ts, link}."""
        out: dict[str, list[dict]] = {s: [] for s in symbols}
        params = {"symbols": ",".join(symbols), "limit": 50, "sort": "desc",
                  "start": since.astimezone(dt.timezone.utc).strftime(
                      "%Y-%m-%dT%H:%M:%SZ")}
        for _ in range(pages):
            data = self._get("/v1beta1/news", params)
            for n in data.get("news", []):
                h = {"title": n.get("headline", ""),
                     "publisher": n.get("source", ""),
                     "ts": parse_ts(n["created_at"]),
                     "link": n.get("url") or ""}
                for sym in n.get("symbols", []):
                    if sym in out:
                        out[sym].append(h)
            params["page_token"] = data.get("next_page_token")
            if not params["page_token"]:
                break
        return out


def google_news(symbol: str) -> list[dict]:
    """Supplementary headlines from Google News RSS (best effort)."""
    import email.utils
    import xml.etree.ElementTree as ET_xml
    q = urllib.parse.quote(f"{symbol} stock when:1d")
    raw = http_get(f"https://news.google.com/rss/search?q={q}"
                   "&hl=en-US&gl=US&ceid=US:en", timeout=10)
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


def merge_headlines(*lists: list[dict]) -> list[dict]:
    seen, uniq = set(), []
    for n in sorted((h for lst in lists for h in lst), key=lambda n: -n["ts"]):
        key = re.sub(r"\W+", "", n["title"].lower())[:60]
        if key and key not in seen:
            seen.add(key)
            uniq.append(n)
    return uniq


def yahoo_fundamentals(symbols: list[str], now: dt.datetime,
                       use_cache: bool = True) -> dict:
    """P/E, analyst rating, market cap and name from Yahoo, fetched at most
    once a day and only attempted every 30 min after a failure. Alpaca has
    no fundamentals; without these the rating uses the other factors."""
    if os.environ.get("YAHOO_FUNDAMENTALS", "1") == "0":
        return {}
    path = os.path.join(CACHE, f"fundamentals-{now.astimezone(ET):%Y%m%d}"
                               ".json")
    cache: dict = load_state(path) if use_cache else {}
    missing = [s for s in symbols if s not in cache.get("quotes", {})]
    if not missing or now.timestamp() - cache.get("failed_at", 0) < 1800:
        return cache.get("quotes", {})
    try:
        try:
            from curl_cffi import requests as cffi  # looks like Chrome
            sess = cffi.Session(impersonate="chrome")

            def get(url: str) -> bytes:
                r = sess.get(url, timeout=15)
                if r.status_code >= 400:
                    raise FetchError(r.status_code, url)
                return r.content
        except ImportError:
            opener = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor(
                    http.cookiejar.CookieJar()))

            def get(url: str) -> bytes:
                return http_get(url, timeout=15, opener=opener)
        try:
            get("https://fc.yahoo.com")
        except Exception:
            pass  # 404 is expected; it still sets the cookie
        crumb = get("https://query1.finance.yahoo.com/v1/test/getcrumb")
        url = ("https://query1.finance.yahoo.com/v7/finance/quote?symbols="
               + urllib.parse.quote(",".join(missing)) + "&crumb="
               + urllib.parse.quote(crumb.decode()))
        for q in json.loads(get(url))["quoteResponse"]["result"]:
            cache.setdefault("quotes", {})[q["symbol"]] = q
        cache.pop("failed_at", None)
    except Exception as e:
        print(f"note: Yahoo fundamentals unavailable ({e}); rating without "
              "valuation/analyst factors", file=sys.stderr)
        cache["failed_at"] = now.timestamp()
    if use_cache:
        save_json(path, cache, prefix="fundamentals-")
    return cache.get("quotes", {})


def save_json(path: str, data: dict, prefix: str = "") -> None:
    """Write a cache file, removing older files with the same prefix."""
    try:
        d = os.path.dirname(path)
        os.makedirs(d, exist_ok=True)
        if prefix:
            for old in os.listdir(d):
                if old.startswith(prefix) and old != os.path.basename(path):
                    os.remove(os.path.join(d, old))
        with open(path, "w") as f:
            json.dump(data, f)
    except OSError:
        pass


@dataclass
class Bars:
    ts: list[int]
    open: list[float]
    high: list[float]
    low: list[float]
    close: list[float]
    volume: list[float]

    @classmethod
    def from_alpaca(cls, rows: list[dict]) -> "Bars":
        return cls([parse_ts(r["t"]) for r in rows],
                   [r["o"] for r in rows], [r["h"] for r in rows],
                   [r["l"] for r in rows], [r["c"] for r in rows],
                   [r["v"] for r in rows])

    def since(self, t0: float) -> "Bars":
        i = next((i for i, t in enumerate(self.ts) if t >= t0), len(self.ts))
        return Bars(*(col[i:] for col in self.cols()))

    def before(self, t0: float) -> "Bars":
        i = next((i for i, t in enumerate(self.ts) if t >= t0), len(self.ts))
        return Bars(*(col[:i] for col in self.cols()))

    def cols(self) -> tuple:
        return (self.ts, self.open, self.high, self.low, self.close,
                self.volume)


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
    factors: dict[str, float | None]


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
    valuation: float | None
    if fpe is None and tpe is None:
        valuation = None  # no data: factor dropped, weights rescaled
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
    analyst: float | None = None
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

    # 6. Liquidity / risk: size tier (neutral 65 when unknown) less a
    #    volatility penalty.
    cap = q.get("marketCap")
    risk = (65 if cap is None else 80 if cap >= 2e11 else 65 if cap >= 1e10
            else 50 if cap >= 2e9 else 30)
    ann_vol = daily_sigma_pct(daily, 60) * math.sqrt(252)
    risk -= 20 if ann_vol > 80 else 10 if ann_vol > 50 else 0
    risk = clamp(risk)

    f = {"catalyst": catalyst, "momentum": momentum, "valuation": valuation,
         "analyst": analyst, "technical": technical, "risk": risk}
    w = {"catalyst": .25, "momentum": .20, "valuation": .20,
         "analyst": .15, "technical": .10, "risk": .10}
    have = [k for k in f if f[k] is not None]
    score = sum(f[k] * w[k] for k in have) / sum(w[k] for k in have)
    bad_news = v.label == "News-driven" and down and v.news_tone == "negative"
    if score >= 68 and catalyst >= 60 and not bad_news:
        label = "Strong Buy"
    elif score >= 56 and not bad_news:
        label = "Buy"
    else:
        label = "Hold"
    return Rating(label, round(score, 1),
                  {k: None if x is None else round(x) for k, x in f.items()})


# ------------------------------------------------------------------- runner

def in_session_window(now: dt.datetime) -> bool:
    et = now.astimezone(ET)
    return (et.weekday() < 5
            and dt.time(9, 35) <= et.time() <= dt.time(16, 5))


def cached_daily(api: Alpaca, symbols: list[str], session_open: dt.datetime,
                 now: dt.datetime) -> dict[str, Bars]:
    """A year of daily bars before the session, fetched once a day for each
    symbol (they only change at the close)."""
    path = os.path.join(CACHE, f"daily-{session_open:%Y%m%d}-{api.feed}.json")
    cache = load_state(path)
    missing = [s for s in symbols if s not in cache]
    if missing:
        cache.update({s: [] for s in missing})
        cache.update(api.bars(missing, "1Day",
                              session_open - dt.timedelta(days=400),
                              session_open, adjustment="split"))
        save_json(path, cache, prefix="daily-")
    return {s: Bars.from_alpaca(cache.get(s, [])).before(
        session_open.timestamp()) for s in symbols}


def last_session(api: Alpaca, now: dt.datetime) -> tuple[dt.datetime, Bars]:
    """Open time of the latest session with SPY trades, and SPY's 5m bars."""
    spy = Bars.from_alpaca(api.bars(["SPY"], "5Min",
                                    now - dt.timedelta(days=6),
                                    now).get("SPY", []))
    if not spy.ts:
        raise RuntimeError("no SPY bars returned; check the Alpaca feed")
    day = dt.datetime.fromtimestamp(spy.ts[-1], ET).date()
    session_open = dt.datetime.combine(day, dt.time(9, 30), ET)
    return session_open, spy.since(session_open.timestamp())


def diagnose() -> None:
    """Check each data source; prints one line per check."""
    now = dt.datetime.now(dt.timezone.utc)
    key, secret, feed = load_keys()
    print(f"Alpaca keys: {'found' if key and secret else 'MISSING'} "
          f"(feed: {feed}, config: {CONFIG})")
    if key and secret:
        api = Alpaca(key, secret, feed)
        checks = [
            ("most actives", lambda: f"{len(api.most_active(5))} symbols"),
            ("5-min bars", lambda: f"{len(last_session(api, now)[1].ts)} "
                                   "SPY bars in latest session"),
            ("news", lambda: f"{len(api.news(['AAPL'], now - dt.timedelta(days=2), 1)['AAPL'])} AAPL headlines"),
        ]
        for name, fn in checks:
            try:
                print(f"  {name:14} OK: {fn()}")
            except Exception as e:
                print(f"  {name:14} FAILED: {e}")
    for name, fn in [
        ("google news", lambda: f"{len(google_news('AAPL'))} headlines"),
        ("yahoo P/E etc.", lambda: "OK" if yahoo_fundamentals(
            ["AAPL"], now, use_cache=False) else
            "unavailable (optional; ratings skip valuation/analyst)"),
    ]:
        try:
            print(f"  {name:14} {fn()}")
        except Exception as e:
            print(f"  {name:14} FAILED: {e}")


def market_open(now: dt.datetime, spy: Bars) -> bool:
    if not in_session_window(now):
        return False
    # Holidays: no fresh SPY bar today.
    return bool(spy.ts) and now.timestamp() - spy.ts[-1] < 20 * 60


def scan(now: dt.datetime, force: bool = False,
         api: Alpaca | None = None) -> tuple[str, list[dict]]:
    api = api or Alpaca.from_config()
    session_open, spy = last_session(api, now)
    if not force and not market_open(now, spy):
        return "", []
    # Analyse "as of" the latest bar, so --force on a weekend replays the
    # last session instead of treating it as live.
    as_of = min(now, session_open + dt.timedelta(hours=6, minutes=30))

    try:
        universe = [s for s in api.most_active(TOP_N + 5) if s != "SPY"]
        universe = universe[:TOP_N]
        source = "Alpaca most actives"
    except Exception as e:
        print(f"warn: most actives unavailable ({e})", file=sys.stderr)
        universe = []
    if not universe:
        universe, source = FALLBACK_TICKERS[:TOP_N], "fallback ticker list"

    intraday = {s: Bars.from_alpaca(rows).since(session_open.timestamp())
                for s, rows in api.bars(universe, "5Min", session_open,
                                        as_of).items()}
    daily = cached_daily(api, universe, session_open, now)
    quotes = yahoo_fundamentals(universe, now)

    flagged: list[tuple[Move, Bars, dict]] = []
    for sym in universe:
        try:
            d, q = daily.get(sym), quotes.get(sym, {})
            if not d or not d.close or sym not in intraday:
                continue
            avg_vol = statistics.fmean(d.volume[-60:])
            m = analyse_move(sym, q.get("shortName") or sym, intraday[sym],
                             d, spy, d.close[-1], avg_vol, as_of)
            if m and (abs(m.move_pct) >= MOVE_PCT
                      or m.move_sigma >= MOVE_SIGMA):
                flagged.append((m, d, q))
        except Exception as e:  # one bad ticker shouldn't kill the run
            print(f"warn: {sym}: {e}", file=sys.stderr)

    news: dict[str, list[dict]] = {}
    if flagged:
        syms = [m.symbol for m, _, _ in flagged]
        try:
            news = api.news(syms, as_of - dt.timedelta(hours=NEWS_LOOKBACK_H))
        except Exception as e:
            print(f"warn: Alpaca news unavailable ({e})", file=sys.stderr)

    results: list[dict] = []
    for m, d, q in flagged:
        try:
            extra = google_news(m.symbol)
        except Exception:
            extra = []
        m.headlines = merge_headlines(news.get(m.symbol, []), extra)
        v = classify(m, as_of)
        results.append({"move": m, "verdict": v, "rating": rate(m, v, q, d)})

    results.sort(key=lambda x: -abs(x["move"].move_pct))
    spy_move = pct(spy.close[-1], spy.open[0]) if spy.close else 0.0
    header = (f"Universe: top {len(universe)} by volume ({source}; "
              f"{api.feed} feed). SPY {spy_move:+.2f}% today. Threshold: "
              f"≥{MOVE_PCT:g}% or ≥{MOVE_SIGMA:g}σ.")
    return render(as_of, header, results), results


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
                    f"{k} {'n/a' if s is None else s}"
                    for k, s in r.factors.items())]
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


def setup() -> None:
    """Ask for Alpaca keys, check them, and save them for scheduled runs."""
    import getpass
    print("Alpaca keys: sign up free at https://alpaca.markets, then in the "
          "dashboard open API Keys and generate a key pair.")
    key = input("API key ID: ").strip()
    secret = getpass.getpass("Secret key (hidden as you type): ").strip()
    feed = input("Data feed [iex]: ").strip() or "iex"
    try:
        n = len(Alpaca(key, secret, feed).most_active(5))
        print(f"Keys work: got {n} most-active symbols.")
    except Exception as e:
        print(f"Those keys didn't work: {e}")
        if input("Save anyway? [y/N] ").strip().lower() != "y":
            return
    os.makedirs(os.path.dirname(CONFIG), exist_ok=True)
    fd = os.open(CONFIG, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump({"key_id": key, "secret_key": secret, "feed": feed}, f)
    print(f"Saved to {CONFIG} (readable only by you).")


# --------------------------------------------------------------- scheduling

TASK = "com.tempore.market-moves"
PLIST = os.path.expanduser(f"~/Library/LaunchAgents/{TASK}.plist")
CRON_TAG = "# market-moves-scanner"


def install() -> None:
    if not all(load_keys()[:2]):
        print("Note: no Alpaca keys saved yet; scheduled runs will fail "
              "until you run: python3 scanner.py --setup")
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
    ap.add_argument("--setup", action="store_true",
                    help="enter and save your Alpaca API keys")
    args = ap.parse_args()

    if args.setup:
        setup()
        return 0

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
