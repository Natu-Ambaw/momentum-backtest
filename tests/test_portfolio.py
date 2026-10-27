import numpy as np
import pandas as pd
import pytest

from momentum.portfolio import quantile_weights


def test_dollar_neutral_and_gross_two():
    sig = pd.Series(np.arange(10, dtype=float), index=list("abcdefghij"))
    w = quantile_weights(sig, n_quantiles=5)
    assert w.sum() == pytest.approx(0.0)
    assert w.abs().sum() == pytest.approx(2.0)
    assert w["i"] == pytest.approx(0.5) and w["j"] == pytest.approx(0.5)
    assert w["a"] == pytest.approx(-0.5) and w["b"] == pytest.approx(-0.5)
    assert (w[list("cdefgh")] == 0).all()


def test_nans_get_zero_weight():
    sig = pd.Series([np.nan, 1, 2, 3, 4, 5, np.nan], index=list("abcdefg"))
    w = quantile_weights(sig, n_quantiles=5)
    assert list(w.index) == list(sig.index)
    assert w["a"] == 0 and w["g"] == 0
    assert w["f"] == pytest.approx(1.0) and w["b"] == pytest.approx(-1.0)


def test_too_few_stocks_returns_zeros():
    sig = pd.Series([1.0, 2.0, np.nan], index=list("abc"))
    w = quantile_weights(sig, n_quantiles=5)
    assert (w == 0).all()
