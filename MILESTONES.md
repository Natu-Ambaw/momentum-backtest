# Milestones

Work top to bottom. Each milestone has tests; run `pytest tests/test_<name>.py`
until they pass, then commit. Don't look up a finished momentum backtest —
interviewers will ask you to explain every line.

## M1 — Data (≈1 evening)
- Read `src/momentum/data.py` (already implemented). Run `python scripts/run_backtest.py --data-only`.
- Write in the README: which tickers, which dates, and **why this universe has survivorship bias**
  (today's large caps were winners by construction). Optional stretch: use CRSP via CMU library access.

## M2 — Returns & signal (≈1 evening) — `signals.py`
- `monthly_returns(prices)` and `momentum_signal(prices, lookback=12, skip=1)`.
- Tests: `test_signals.py`, `test_no_lookahead.py`.
- Interview question to be ready for: *why skip the most recent month?* (short-term reversal).

## M3 — Portfolio formation (≈1 evening) — `portfolio.py`
- `quantile_weights(signal_row, n_quantiles=5)` → dollar-neutral long/short weights.
- Tests: `test_portfolio.py` (weights sum to 0, gross exposure 2, NaNs excluded).

## M4 — Backtest engine with costs (≈2 evenings) — `backtest.py`
- `run_backtest(prices, ..., cost_bps=10)` → monthly gross return, net return, turnover.
- Key detail: weights formed at end of month *t* earn returns over month *t+1*.
- Tests: `test_backtest.py`.

## M5 — Metrics (≈1 evening) — `metrics.py`
- `annualized_sharpe`, `max_drawdown`, `annualized_turnover`.
- Tests: `test_metrics.py`.

## M6 — Make it credible (≈1 week)
- Cost sensitivity: net Sharpe at 0, 5, 10, 25, 50 bps.
- Walk-forward: choose lookback on 2000–2012 only, report 2013–present.
- Regress net returns on Fama-French factors (MOM included) from Ken French's site; report alpha t-stat.
- Plot: cumulative returns, rolling 36-month Sharpe, drawdowns. Note the 2009 momentum crash.

## M7 — Write-up
- Fill in README Results + biases table. One honest paragraph on what *didn't* work.
- Pin the repo on your GitHub profile and add one resume bullet with a number in it.
