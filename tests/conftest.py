import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def toy_prices() -> pd.DataFrame:
    """3 stocks, 6 month-ends, hand-checkable prices."""
    idx = pd.date_range("2020-01-31", periods=6, freq="ME")
    return pd.DataFrame(
        {
            "A": [100, 110, 121, 133.1, 146.41, 161.051],  # +10%/month
            "B": [100, 100, 100, 100, 100, 100],            # flat
            "C": [np.nan, 50, 45, 40.5, 36.45, 32.805],     # lists late, -10%/month
        },
        index=idx,
    )


@pytest.fixture
def random_prices() -> pd.DataFrame:
    rng = np.random.default_rng(0)
    idx = pd.date_range("2005-01-31", periods=60, freq="ME")
    rets = rng.normal(0.01, 0.08, size=(60, 20))
    return pd.DataFrame(100 * np.cumprod(1 + rets, axis=0), index=idx,
                        columns=[f"S{i}" for i in range(20)])
