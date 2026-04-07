# Velo: Vectorized Backtesting Engine

**Velo** is a high-performance quantitative backtesting framework built in Python. Unlike traditional loop-based backtesters, Velo utilizes **Vectorized Operations** via NumPy and Pandas to simulate trading strategies across large historical datasets in $O(1)$ time relative to the number of signals.

## 📈 Key Features

- **Vectorized Signal Generation:** Uses rolling window statistics (SMA) to generate trade signals across thousands of data points simultaneously.
- **Look-ahead Bias Protection:** Implements strict $t+1$ execution logic via index shifting to ensure realistic backtest results.
- **Continuous Return Modeling:** Utilizes Logarithmic Returns for time-additivity and numerical stability in multi-period performance tracking.
- **Risk Attribution:** Calculates industry-standard metrics including Annualized Sharpe Ratio and Maximum Drawdown (MDD).

## 🧮 Mathematical Framework

### Log Returns
To maintain additive properties across time horizons:
$$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$$

### Risk-Adjusted Return (Sharpe)
Measures the excess return per unit of volatility:
$$Sharpe = \frac{\overline{r}}{\sigma_r} \cdot \sqrt{252}$$

### Maximum Drawdown
Quantifies the "Worst Case Scenario" peak-to-trough decline:
$$MDD = \max\left(\frac{Peak_t - Value_t}{Peak_t}\right)$$

## 🛠️ Usage

### Prerequisites
```bash
pip install pandas numpy yfinance
