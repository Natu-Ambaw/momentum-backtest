"""M4 — the backtest engine. YOU implement this."""
from __future__ import annotations

import pandas as pd

from momentum.portfolio import quantile_weights
from momentum.signals import momentum_signal, monthly_returns


def run_backtest(
    prices: pd.DataFrame,
    lookback: int = 12,
    skip: int = 1,
    n_quantiles: int = 5,
    cost_bps: float = 10.0,
) -> pd.DataFrame:
    """Monthly long/short momentum backtest.

    Steps:
      1. rets = monthly_returns(prices); sig = momentum_signal(prices, lookback, skip)
      2. For each month t: w_t = quantile_weights(sig.loc[t], n_quantiles)
      3. The weights chosen at the END of month t earn the returns of month t+1:
             gross_{t+1} = sum_i w_{t,i} * r_{t+1,i}     (treat NaN returns as 0)
      4. turnover_t = sum_i |w_{t,i} - w_{t-1,i}|      (first month: vs. all-zero weights)
         cost_{t+1}  = turnover_t * cost_bps / 10_000
         net_{t+1}   = gross_{t+1} - cost_{t+1}

    Return a DataFrame indexed by the month the return is EARNED (t+1), with
    columns ["gross", "net", "turnover"]. Drop months before the first
    non-zero portfolio, and drop the final formation month (no t+1 return yet).
    """
    raise NotImplementedError("M4: implement run_backtest")
