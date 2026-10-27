"""Price data loading (provided — you don't need to modify this for M1).

Downloads daily adjusted closes from Yahoo Finance, caches them to parquet,
and resamples to month-end. Output: DataFrame indexed by month-end date,
one column per ticker, NaN where a stock didn't trade yet.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

CACHE_DIR = Path(__file__).resolve().parents[2] / "data" / "cache"

# A starter universe of large U.S. stocks across sectors.
# WARNING: picking *today's* big companies bakes in survivorship bias —
# document this in the README (milestone M1).
DEFAULT_UNIVERSE = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "META", "NVDA", "JPM", "BAC", "WFC", "C",
    "GS", "MS", "XOM", "CVX", "COP", "JNJ", "PFE", "MRK", "ABT", "UNH",
    "PG", "KO", "PEP", "WMT", "COST", "HD", "LOW", "MCD", "NKE", "DIS",
    "INTC", "CSCO", "ORCL", "IBM", "QCOM", "TXN", "AMD", "ADBE", "CRM", "NFLX",
    "CAT", "DE", "BA", "GE", "HON", "MMM", "UPS", "FDX", "LMT", "RTX",
    "T", "VZ", "CMCSA", "NEE", "DUK", "SO", "D", "AMGN", "GILD", "BMY",
    "LLY", "MDT", "TMO", "DHR", "SBUX", "TGT", "F", "GM", "AXP", "USB",
    "PNC", "BK", "MO", "PM", "CL", "KMB", "GIS", "K", "HSY", "MDLZ",
    "SLB", "HAL", "OXY", "EOG", "APA", "FCX", "NEM", "DOW", "DD", "LIN",
    "SPG", "PLD", "AMT", "CCI", "EQIX", "AIG", "MET", "PRU", "ALL", "TRV",
]


def load_monthly_prices(
    tickers: list[str] | None = None,
    start: str = "2000-01-01",
    end: str | None = None,
    use_cache: bool = True,
) -> pd.DataFrame:
    """Return month-end adjusted close prices (rows = months, cols = tickers)."""
    tickers = tickers or DEFAULT_UNIVERSE
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache = CACHE_DIR / f"daily_{start}_{end or 'latest'}_{len(tickers)}.parquet"

    if use_cache and cache.exists():
        daily = pd.read_parquet(cache)
    else:
        import yfinance as yf

        raw = yf.download(tickers, start=start, end=end, auto_adjust=True, progress=False)
        daily = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
        daily.to_parquet(cache)

    monthly = daily.resample("ME").last()
    return monthly.dropna(how="all")
