# Market move scanner

[`scanner.py`](scanner.py) runs on your own computer every 5 minutes during US market hours (9:30–16:00 ET, weekdays). Each run:

1. Takes the 25 most traded US stocks from Alpaca's market data API.
2. Flags large moves: at least 3% from the prior close, or at least 2 daily standard deviations.
3. Decides whether each move is **news-driven** or **automated / flow-driven selling (or buying)**.
4. Rates the stock **Strong Buy**, **Buy** or **Hold**.
5. Saves the results and alerts you:
   - `reports/latest.html` (and `latest.md`): every current large move, with details.
   - `reports/<date>.md`: new or changed signals only.
   - An alert for new signals, with an **Open details** button, so you never have to check the terminal.

It needs Python 3.9 or later and a free [Alpaca](https://alpaca.markets) account. No packages to install. Not investment advice.

## Setup

1. **Get Alpaca keys.** Sign up at [alpaca.markets](https://alpaca.markets): a free paper-trading account is enough. In the dashboard, open **API Keys** and generate a key pair. The secret is only shown once, so keep the page open.
2. **Save the keys and start the scanner:**

```sh
python3 scanner.py --setup              # paste the key ID and secret; checks them and saves them
python3 scanner.py --force --no-alert   # one test run, even if the market is closed
python3 scanner.py --install            # scan every 5 minutes from now on
```

`--setup` saves the keys to `~/.config/market-moves-scanner/alpaca.json`, readable only by you. Scheduled runs don't see your shell's environment variables, which is why the keys go in a file. Setting `ALPACA_API_KEY_ID` and `ALPACA_API_SECRET_KEY` in the environment overrides the file.

`--install` uses your operating system's own scheduler:

| OS | Scheduler | Remove with |
|---|---|---|
| macOS | launchd agent `~/Library/LaunchAgents/com.tempore.market-moves.plist` | `python3 scanner.py --uninstall` |
| Linux | a `crontab` line tagged `# market-moves-scanner` (weekdays, every 5 min) | `python3 scanner.py --uninstall` |
| Windows | Task Scheduler task `MarketMoveScanner` (use `py scanner.py --install`) | `py scanner.py --uninstall` |

The scheduler fires every 5 minutes. Outside market hours the script exits at once without touching the network, and on holidays it exits after a single SPY price check. Run output and errors go to `reports/scanner.log`.

The computer has to be awake for scans to run. If you'd rather keep it in a terminal window than install a schedule, run `python3 scanner.py --every 5`.

## Notifications

You don't need to watch the terminal. When a scan finds new or changed signals, you get an alert listing them:

> **Market moves: 2 new signal(s)**
> NVDA −4.9% → Buy
> Automated selling · $118.20 · score 64.5
> No catalyst headlines found; steady, evenly sized bars (execution-algo footprint)
>
> [Dismiss] **[Open details]**

**Open details** opens `reports/latest.html` in your browser. It shows every current large move with its driver, evidence, headlines (linked) and factor scores, and marks the new ones. The alert closes by itself after 4 minutes if you don't click it.

**On your phone:** the details page is laid out for phone screens (checked at iPhone SE, iPhone 15 Pro Max and Pixel 7 widths, light and dark mode). On a Mac with iCloud Drive turned on, every scan also saves it to **iCloud Drive → Market Moves → latest.html**. On an iPhone, open the Files app, go to that folder and tap the file. It updates with each scan, and headline links open in Safari. To save it somewhere else instead (Dropbox, Google Drive…), set `PHONE_DIR` to that folder; `PHONE_DIR=` turns the copy off.

- **No repeats:** the same stock doesn't alert again that day unless its driver or rating changes, or the move grows by 2 more points.
- **Quiet when nothing happens:** scans that find nothing stay silent.
- **Failure alerts:** if scheduled scans start failing (bad keys, no internet), you get one "scans failing" alert per day, with an **Open log** button, until a scan succeeds.

`python3 scanner.py --test-notification` shows a sample alert. Its **Open details** button opens a sample page.

- **macOS:** the alert above works without extra setup or permissions. If you prefer Notification Center banners, set `MAC_NOTIFY=banner`. Clicking a plain banner opens Script Editor, because macOS doesn't let scripts choose what a click does. With terminal-notifier (`brew install terminal-notifier`) and its notifications allowed in System Settings → Notifications, a click opens the details page instead.
- **Linux:** one `notify-send` banner per signal (package `libnotify-bin` on Debian/Ubuntu). It works from cron too.
- **Windows:** one system-tray balloon per signal.

`--no-alert` turns notifications off.

## News vs automated selling

Each move gets a news score and a flow score from 0 to 100. If one leads by 15 points or more, it sets the label. Otherwise the label is "Mixed / unclear".

| Points toward **news-driven** | Points toward **automated / flow-driven** |
|---|---|
| Catalyst headlines (earnings, guidance, FDA, M&A, rating changes, probes, offerings…) in the last 18h (Alpaca's Benzinga news feed and Google News) | No catalyst headlines at all |
| Headline timestamp within 45 min of the biggest bar, or before a gap open | Move explained by SPY beta (high intraday correlation) |
| Most of the move came in the opening gap | Steady run of similar-sized bars in one direction: the footprint of a TWAP/VWAP execution algo |
| One 5-minute bar made at least 35% of the move | High volume spread evenly across bars rather than in spikes |
| Move is idiosyncratic (little explained by the market) | Large retrace from the extreme (stop cascade or forced liquidation) |
| | Move concentrated after 15:45 ET (market-on-close imbalance), or on an options-expiry / index-rebalance Friday |

## Rating

The rating is a weighted composite of six factors, each scored 0 to 100. These are the factors fundamental long/short funds screen on:

| Factor | Weight | What it measures |
|---|---|---|
| Catalyst quality | 25% | Flow-driven selling in a sound name is a dislocation (80). Negative fundamental news is not (20). Positive news on an up move gets credit for post-earnings drift (75). |
| Momentum / trend | 20% | 12-1 month return, price vs 50/200-day averages, golden/death cross, proximity to the 52-week high |
| Valuation | 20% | When available: forward P/E band plus implied EPS growth (trailing P/E vs forward P/E, PEG < 1 bonus) |
| Analyst consensus | 15% | Yahoo's average analyst rating, when available (1 = strong buy … 5 = sell) |
| Technicals | 10% | Daily RSI(14): oversold scores higher. Bonus for a 2.5σ+ flow-driven drop. |
| Liquidity / risk | 10% | Market cap tier (neutral when unknown), with a penalty for annualised volatility above 50% or 80% |

Factors without data are left out and the remaining weights are scaled to add up to 100%. A score of 68 or more with catalyst ≥ 60 rates **Strong Buy**. A score of 56 or more rates **Buy**. Everything else rates **Hold**. A news-driven drop on negative headlines is always **Hold**.

## Data sources

| Data | Source |
|---|---|
| Most traded stocks, 5-minute and daily price bars | Alpaca market data (free plan: 200 requests/min) |
| Headlines | Alpaca news (Benzinga), plus Google News RSS |
| P/E, analyst rating, market cap, company name | Yahoo Finance (optional; see below) |

A scan makes about 4 Alpaca requests. Daily bars are fetched once a day and cached in `reports/.cache/`.

**Data feed.** The free plan's real-time bars come from the IEX exchange (`iex`), which handles only a few percent of US volume. Prices track the market closely, and relative-volume figures stay consistent because every bar comes from the same feed. For full-market volume, choose `delayed_sip` during `--setup` (free, 15 minutes behind) or `sip` (paid, real time). You can also set it with the `ALPACA_FEED` environment variable.

**Valuation and analyst data** come from Yahoo Finance, fetched at most once a day. Alpaca doesn't provide them. If Yahoo blocks the request (HTTP 429), the scanner retries every 30 minutes. In the meantime those two factors show as `n/a`, and the rating uses the other four factors with their weights scaled up. Installing `curl_cffi` (`python3 -m pip install curl_cffi`) usually gets past Yahoo's block. Set `YAHOO_FUNDAMENTALS=0` to skip Yahoo entirely.

## Options

- `--force`: run even when the market is closed (uses the last session's data).
- `--no-alert`: skip desktop notifications.
- `--test-notification`: show a sample alert.
- `--every MIN`: keep running and scan every MIN minutes.
- `--setup`: enter, check and save your Alpaca keys and data feed.
- `--diagnose`: test each data source and print which ones respond. Use it when a scan fails.
- **Thresholds:** set the `TOP_N`, `MOVE_PCT` and `MOVE_SIGMA` environment variables. `REPORTS_DIR` moves the reports folder.
- **Tests:** `python3 -m unittest test_scanner.py` (offline, synthetic data).

## Limits

- If Alpaca's most-actives list fails, the scanner falls back to a fixed list of high-volume tickers.
- With the free `iex` feed, a thinly traded stock can have gaps in its 5-minute bars, which weakens the volume-profile signals for that stock.
- Scans only run while the computer is on and awake. A sleeping laptop misses them.
