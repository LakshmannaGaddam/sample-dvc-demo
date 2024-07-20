print("Hello")

from datetime import date
from nsepy import get_history
import pandas as pd

# Get list of all NSE stocks
all_stock_codes = pd.read_csv('https://archives.nseindia.com/content/equities/EQUITY_L.csv')

# Initialize an empty DataFrame to store closing prices
closing_prices = pd.DataFrame()

# Define start and end dates for fetching data
start_date = date(2024, 1, 1)
end_date = date(2024, 5, 6)  # Adjust end date as per your requirement

# Iterate over all stocks and fetch closing prices
for index, row in all_stock_codes.iterrows():
    symbol = row['SYMBOL']
    try:
        data = get_history(symbol=symbol, start=start_date, end=end_date)
        closing_prices[symbol] = data['Close']
    except:
        print(f"Failed to fetch data for {symbol}")

# Save the closing prices to a CSV file
closing_prices.to_csv('closing_prices.csv')

# Display the closing prices DataFrame
print(closing_prices)

print(all_stock_codes.head())

print(all_stock_codes.columns)

data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))

print(data)