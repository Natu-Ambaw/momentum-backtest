"""Entry point. `python scripts/run_backtest.py [--data-only] [--cost-bps 10]`"""
import argparse

from momentum.data import load_monthly_prices


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--data-only", action="store_true")
    p.add_argument("--cost-bps", type=float, default=10.0)
    args = p.parse_args()

    prices = load_monthly_prices()
    print(f"Loaded {prices.shape[1]} tickers, {prices.index[0]:%Y-%m} to {prices.index[-1]:%Y-%m}")
    print(f"Tickers with full history: {prices.notna().all().sum()}")
    if args.data_only:
        return

    from momentum.backtest import run_backtest
    from momentum.metrics import annualized_sharpe, annualized_turnover, max_drawdown

    bt = run_backtest(prices, cost_bps=args.cost_bps)
    for col in ("gross", "net"):
        print(f"{col:>5}  Sharpe {annualized_sharpe(bt[col]):5.2f}   MaxDD {max_drawdown(bt[col]):6.1%}")
    print(f"Annual turnover: {annualized_turnover(bt['turnover']):.1f}x")
    # M6: add plots and Fama-French regression here (or in a notebook).


if __name__ == "__main__":
    main()
