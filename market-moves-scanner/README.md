# Market move scanner

[`scanner.py`](scanner.py) runs on your own computer every 5 minutes during US market hours (9:30–16:00 ET, weekdays). Each run:

1. Takes the 25 most traded US stocks (Yahoo Finance "most actives").
2. Flags large moves: at least 3% from the prior close, or at least 2 daily standard deviations.
3. Decides whether each move is **news-driven** or **automated / flow-driven selling (or buying)**.
4. Rates the stock **Strong Buy**, **Buy** or **Hold**.
5. Saves the results and alerts you:
   - `reports/latest.md`: the full table from the latest run.
   - `reports/<date>.md`: new or changed signals only.
   - A desktop notification for each batch of new signals.

It needs only Python 3.9 or later: no packages, accounts or API keys. Not investment advice.

## Setup

```sh
git clone https://github.com/Tempore-dev/research && cd research/market-moves-scanner
python3 scanner.py --force --no-alert   # one test run, even if the market is closed
python3 scanner.py --install            # scan every 5 minutes from now on
```

`--install` uses your operating system's own scheduler:

| OS | Scheduler | Remove with |
|---|---|---|
| macOS | launchd agent `~/Library/LaunchAgents/com.tempore.market-moves.plist` | `python3 scanner.py --uninstall` |
| Linux | a `crontab` line tagged `# market-moves-scanner` (weekdays, every 5 min) | `python3 scanner.py --uninstall` |
| Windows | Task Scheduler task `MarketMoveScanner` (use `py scanner.py --install`) | `py scanner.py --uninstall` |

The scheduler fires every 5 minutes. Outside market hours the script exits at once without touching the network, and on holidays it exits after a single price check. Run output and errors go to `reports/scanner.log`.

The computer has to be awake for scans to run. If you'd rather keep it in a terminal window than install a schedule, run `python3 scanner.py --every 5`.

Linux notifications use `notify-send` (package `libnotify-bin` on Debian/Ubuntu). On macOS, the first notification may ask you to allow alerts from Script Editor.

## News vs automated selling

Each move gets a news score and a flow score from 0 to 100. If one leads by 15 points or more, it sets the label. Otherwise the label is "Mixed / unclear".

| Points toward **news-driven** | Points toward **automated / flow-driven** |
|---|---|
| Catalyst headlines (earnings, guidance, FDA, M&A, rating changes, probes, offerings…) in the last 18h (Yahoo Finance and Google News) | No catalyst headlines at all |
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
| Valuation | 20% | Forward P/E band plus implied EPS growth (trailing P/E vs forward P/E, PEG < 1 bonus) |
| Analyst consensus | 15% | Yahoo's average analyst rating (1 = strong buy … 5 = sell) |
| Technicals | 10% | Daily RSI(14): oversold scores higher. Bonus for a 2.5σ+ flow-driven drop. |
| Liquidity / risk | 10% | Market cap tier, with a penalty for annualised volatility above 50% or 80% |

A score of 68 or more with catalyst ≥ 60 rates **Strong Buy**. A score of 56 or more rates **Buy**. Everything else rates **Hold**. A news-driven drop on negative headlines is always **Hold**.

## Options

- `--force`: run even when the market is closed (uses the last session's data).
- `--no-alert`: skip desktop notifications.
- `--every MIN`: keep running and scan every MIN minutes.
- **Thresholds:** set the `TOP_N`, `MOVE_PCT` and `MOVE_SIGMA` environment variables. `REPORTS_DIR` moves the reports folder.
- **Tests:** `python3 -m unittest test_scanner.py` (offline, synthetic data).

## Limits

- Yahoo Finance's endpoints are unofficial and can change or rate-limit without notice. If the most-actives list fails, the scanner falls back to a fixed list of high-volume tickers.
- Scans only run while the computer is on and awake. A sleeping laptop misses them.
