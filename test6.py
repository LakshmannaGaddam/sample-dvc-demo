import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the ticker symbol
ticker_symbol = 'AAPL'  # Example: Apple Inc.

# Fetch historical data
stock_data = yf.download(ticker_symbol, start='2020-01-01', end='2023-01-01')

# Calculate 50-day and 200-day moving averages
stock_data['50_MA'] = stock_data['Adj Close'].rolling(window=50).mean()
stock_data['200_MA'] = stock_data['Adj Close'].rolling(window=200).mean()

# Plotting closing price and moving averages
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Adj Close'], label='Adjusted Close Price')
plt.plot(stock_data['50_MA'], label='50-day Moving Average')
plt.plot(stock_data['200_MA'], label='200-day Moving Average')
plt.title(f'{ticker_symbol} Stock Analysis')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Calculate daily returns
stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()

# Calculate cumulative returns
stock_data['Cumulative_Return'] = (1 + stock_data['Daily_Return']).cumprod() - 1

# Print summary statistics
print(stock_data[['Adj Close', 'Daily_Return', 'Cumulative_Return']].describe())

# Visualize cumulative returns
plt.figure(figsize=(10, 5))
plt.plot(stock_data['Cumulative_Return'], label='Cumulative Return')
plt.title(f'{ticker_symbol} Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.grid(True)
plt.show()
