import yfinance as yf
import pandas as pd

# define the ticker symbol and timeframe
ticker = "AAPL"
start_date = "2020-01-01"
end_date = "2026-01-01"

# download the historical data
data = yf.download(ticker, start=start_date, end=end_date)

# save to csv
data.to_csv("AAPL_data.csv")
print("Data downloaded and saved to AAPL_data.csv")