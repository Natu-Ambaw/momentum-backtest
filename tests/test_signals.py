import numpy as np
import pytest

from momentum.signals import momentum_signal, monthly_returns


def test_monthly_returns_values(toy_prices):
    r = monthly_returns(toy_prices)
    assert r.shape == toy_prices.shape
    assert r.iloc[0].isna().all()
    assert r["A"].iloc[1:].round(10).eq(0.10).all()
    assert r["B"].iloc[1:].eq(0.0).all()


def test_monthly_returns_no_fill(toy_prices):
    r = monthly_returns(toy_prices)
    assert np.isnan(r["C"].iloc[1]), "C had no price in Jan, so Feb return must be NaN"


def test_momentum_signal_formula(toy_prices):
    # lookback=3, skip=1 at row 4: P[3]/P[1] - 1
    s = momentum_signal(toy_prices, lookback=3, skip=1)
    assert s["A"].iloc[4] == pytest.approx(133.1 / 110 - 1)
    assert s["C"].iloc[4] == pytest.approx(40.5 / 50 - 1)


def test_momentum_signal_needs_history(toy_prices):
    s = momentum_signal(toy_prices, lookback=3, skip=1)
    assert s.iloc[:3].isna().all().all()
