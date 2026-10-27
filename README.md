# Cross-Sectional Momentum Backtest

A from-scratch, bias-aware backtest of the 12-1 cross-sectional momentum factor
(Jegadeesh & Titman, 1993) on U.S. equities, with transaction costs and
walk-forward evaluation.

> **Status:** work in progress — see [`MILESTONES.md`](MILESTONES.md).

## Question

Does buying recent winners and shorting recent losers still earn a premium
after realistic trading costs, and how stable is that premium over time?

## Method (fill in as you build)

1. **Universe & data** — monthly adjusted closes for a fixed ticker universe (`src/momentum/data.py`).
2. **Signal** — trailing 12-month return, skipping the most recent month (`signals.py`).
3. **Portfolios** — sort into quantiles each month; long top, short bottom (`portfolio.py`).
4. **Backtest** — hold for one month, charge costs on turnover (`backtest.py`).
5. **Evaluation** — Sharpe, drawdown, turnover, alpha vs. Fama-French factors (`metrics.py`).

## Biases I controlled for

| Bias | How it's handled |
|---|---|
| Look-ahead | Signal at month *t* uses only prices through *t*; returns earned in *t+1*. Enforced by `tests/test_no_lookahead.py`. |
| Survivorship | _TODO: describe your universe and its limitations._ |
| Costs | _TODO: cost model (bps per unit turnover) and sensitivity._ |
| Overfitting | _TODO: parameters chosen in-sample, reported out-of-sample._ |

## Results

_TODO: equity curve, table of metrics, cost-sensitivity chart, 3–5 sentence takeaway._

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest                      # milestone tests (most fail until you implement them)
python scripts/run_backtest.py
```
