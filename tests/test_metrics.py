import numpy as np
import pandas as pd
import pytest

from momentum.metrics import annualized_sharpe, annualized_turnover, max_drawdown


def test_sharpe():
    r = pd.Series([0.01, 0.03, -0.01, 0.02, np.nan])
    expected = r.mean() / r.std(ddof=1) * np.sqrt(12)
    assert annualized_sharpe(r) == pytest.approx(expected)


def test_max_drawdown():
    r = pd.Series([0.10, -0.20, 0.05, -0.10, 0.50])
    eq = np.cumprod(1 + r.values)  # 1.1, .88, .924, .8316, 1.2474
    assert max_drawdown(r) == pytest.approx(0.8316 / 1.1 - 1)


def test_max_drawdown_from_start():
    assert max_drawdown(pd.Series([-0.5, 0.1])) == pytest.approx(-0.5)


def test_no_drawdown():
    assert max_drawdown(pd.Series([0.01, 0.02])) == 0.0


def test_turnover():
    assert annualized_turnover(pd.Series([0.5, 1.5])) == pytest.approx(12.0)
