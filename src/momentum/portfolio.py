"""M3 — portfolio formation. YOU implement this."""
from __future__ import annotations

import pandas as pd


def quantile_weights(signal_row: pd.Series, n_quantiles: int = 5) -> pd.Series:
    """Dollar-neutral, equal-weighted long/short weights for ONE month.

    - Drop NaN signals (those stocks get weight 0 in the output).
    - Rank remaining stocks into `n_quantiles` groups by signal.
      Hint: `pd.qcut(signal.rank(method="first"), n_quantiles, labels=False)`.
    - Top quantile: each stock gets +1 / (number of stocks in top).
    - Bottom quantile: each stock gets -1 / (number of stocks in bottom).
    - Everything else: 0.

    Returns a Series with the SAME index as `signal_row`.
    So: weights.sum() == 0 and weights.abs().sum() == 2.
    If fewer than `n_quantiles` stocks have a signal, return all zeros.
    """
    raise NotImplementedError("M3: implement quantile_weights")
