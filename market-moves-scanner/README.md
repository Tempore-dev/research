# Market move scanner

A GitHub Actions job ([`.github/workflows/market-moves.yml`](../.github/workflows/market-moves.yml)) runs [`scanner.py`](scanner.py) every 5 minutes during US market hours. Each run:

1. Takes the 25 most traded US stocks (Yahoo Finance "most actives").
2. Flags large moves: at least 3% from the prior close, or at least 2 daily standard deviations.
3. Decides whether each move is **news-driven** or **automated / flow-driven selling (or buying)**.
4. Rates the stock **Strong Buy**, **Buy** or **Hold**.
5. Writes the full table to the run's job summary. New or changed signals are posted as a comment on the **Market move alerts** issue. Subscribe to that issue to get notified.

Standard library only. Not investment advice.

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

## Running and tuning

- **Run it now:** Actions tab → *Market move scanner* → *Run workflow*. Tick *force* to run outside market hours.
- **Run locally:** `python3 scanner.py --force --no-alert`
- **Tests:** `python3 -m unittest test_scanner.py` (offline, synthetic data)
- **Thresholds:** set the `TOP_N`, `MOVE_PCT` and `MOVE_SIGMA` environment variables in the workflow.

## Limits

- Yahoo Finance's endpoints are unofficial and can change or rate-limit without notice. If the most-actives list fails, the scanner falls back to a fixed list of high-volume tickers.
- GitHub can delay scheduled runs by several minutes when runners are busy. It also disables scheduled workflows after 60 days with no repository activity.
- Each run bills at least one Actions minute. That comes to about 80 minutes per trading day, or roughly 1,700 a month. This is free on public repositories but counts against the monthly quota on private ones.
