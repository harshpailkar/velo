import pandas as pd
import numpy as np

class Velo:
    def __init__(self, data):
        """
        :param data: A pandas DataFrame with 'Date' and 'Close' columns
        """
        self.df = data.copy()
        
    def prepare_data(self):
        self.df['log_returns'] = np.log(self.df['Close'] / self.df['Close'].shift(1))
        
    def generate_signals(self, short_window=5, long_window=20):
        self.df['sma_short'] = self.df['Close'].rolling(window=short_window).mean()
        self.df['sma_long'] = self.df['Close'].rolling(window=long_window).mean()
        
        self.df['position'] = np.where(self.df['sma_short'] > self.df['sma_long'], 1, 0)
        self.df['position'] = self.df['position'].shift(1)

    def calculate_performance(self):
        self.df['strategy_returns'] = self.df['position'] * self.df['log_returns']
        
        self.df['cum_returns'] = self.df['strategy_returns'].cumsum().apply(np.exp)

        active_returns = self.df['strategy_returns'].dropna()

        if active_returns.std() != 0:
            daily_sharpe = active_returns.mean() / active_returns.std()
            annual_sharpe = daily_sharpe * np.sqrt(252)
        else:
            annual_sharpe = 0

        print(f"Annualized Sharpe Ratio: {annual_sharpe:.2f}")
        return annual_sharpe