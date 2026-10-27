"""M2 — returns and the momentum signal. YOU implement these."""
from __future__ import annotations

import pandas as pd


def monthly_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Simple monthly returns: r_t = P_t / P_{t-1} - 1.

    The first row should be NaN. Don't fill NaNs (a stock that hasn't
    listed yet has no return).
    Hint: one pandas method does this — but make sure it doesn't
    forward-fill missing prices (check its `fill_method` argument).
    """
    raise NotImplementedError("M2: implement monthly_returns")


def momentum_signal(prices: pd.DataFrame, lookback: int = 12, skip: int = 1) -> pd.DataFrame:
    """Trailing return from month t-lookback to month t-skip, known at end of month t.

        signal_t = P_{t-skip} / P_{t-lookback} - 1

    With the defaults (12, 1) this is the classic "12-1" momentum.
    Rows without enough history must be NaN.

    Look-ahead rule: the value at row t may only use prices at rows <= t.
    """
    raise NotImplementedError("M2: implement momentum_signal")
