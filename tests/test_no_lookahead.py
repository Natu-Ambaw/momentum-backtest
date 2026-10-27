"""If changing a FUTURE price changes a PAST signal, you have look-ahead bias."""
import pandas as pd

from momentum.signals import momentum_signal


def test_future_prices_do_not_change_past_signal(random_prices):
    base = momentum_signal(random_prices)
    shocked = random_prices.copy()
    shocked.iloc[40:] *= 3.0  # wreck the future
    after = momentum_signal(shocked)
    pd.testing.assert_frame_equal(base.iloc[:40], after.iloc[:40])
