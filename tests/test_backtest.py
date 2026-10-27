import numpy as np
import pandas as pd
import pytest

from momentum.backtest import run_backtest


def _trend_prices():
    """10 stocks with constant monthly growth rates -> momentum must win."""
    idx = pd.date_range("2010-01-31", periods=24, freq="ME")
    growth = np.linspace(-0.02, 0.02, 10)
    data = {f"S{i}": 100 * (1 + g) ** np.arange(24) for i, g in enumerate(growth)}
    return pd.DataFrame(data, index=idx)


def test_columns_and_timing():
    bt = run_backtest(_trend_prices(), lookback=3, skip=1, n_quantiles=5, cost_bps=0)
    assert list(bt.columns) == ["gross", "net", "turnover"]
    # first signal at row 3 -> first earned return at row 4; last row earns from row 22's weights
    idx = _trend_prices().index
    assert bt.index[0] == idx[4]
    assert bt.index[-1] == idx[-1]


def test_trend_gross_return_is_exact():
    bt = run_backtest(_trend_prices(), lookback=3, skip=1, n_quantiles=5, cost_bps=0)
    g = np.linspace(-0.02, 0.02, 10)
    expected = 0.5 * (g[8] + g[9]) - 0.5 * (g[0] + g[1])
    assert np.allclose(bt["gross"], expected)


def test_costs_only_on_turnover():
    bt = run_backtest(_trend_prices(), lookback=3, skip=1, n_quantiles=5, cost_bps=100)
    # ranks never change: full turnover (2.0) only on the first rebalance
    assert bt["turnover"].iloc[0] == pytest.approx(2.0)
    assert np.allclose(bt["turnover"].iloc[1:], 0.0)
    assert bt["net"].iloc[0] == pytest.approx(bt["gross"].iloc[0] - 2.0 * 0.01)
    assert np.allclose(bt["net"].iloc[1:], bt["gross"].iloc[1:])
