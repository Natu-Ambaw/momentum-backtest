"""M5 — performance metrics. YOU implement these (no libraries like empyrical!)."""
from __future__ import annotations

import pandas as pd


def annualized_sharpe(monthly_returns: pd.Series, periods_per_year: int = 12) -> float:
    """mean / std * sqrt(periods_per_year). Use sample std (ddof=1). Ignore NaNs.

    (We treat the long/short return as already an excess return — why is that
    reasonable for a dollar-neutral portfolio? Put the answer in the README.)
    """
    raise NotImplementedError("M5: implement annualized_sharpe")


def max_drawdown(monthly_returns: pd.Series) -> float:
    """Largest peak-to-trough decline of the compounded equity curve.

    equity = (1 + r).cumprod(); drawdown = equity / running_max - 1.
    Return a NEGATIVE number (e.g. -0.35 for a 35% drawdown); 0.0 if none.
    Note: the starting value of 1.0 counts as a peak.
    """
    raise NotImplementedError("M5: implement max_drawdown")


def annualized_turnover(turnover: pd.Series, periods_per_year: int = 12) -> float:
    """Average monthly turnover * periods_per_year."""
    raise NotImplementedError("M5: implement annualized_turnover")
