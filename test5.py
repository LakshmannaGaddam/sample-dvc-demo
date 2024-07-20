import requests
import pandas as pd

# Your Alpha Vantage API key
api_key = '17SM8GH70SYUPUNI'

def fetch_balance_sheet_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    annual_reports = data.get('annualReports', [])
    balance_sheet = pd.DataFrame(annual_reports)
    while 'nextPage' in data:
        next_page_url = f"{url}&page={data['nextPage']}"
        response = requests.get(next_page_url)
        data = response.json()
        annual_reports = data.get('annualReports', [])
        balance_sheet = balance_sheet.append(pd.DataFrame(annual_reports), ignore_index=True)
    return balance_sheet

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
balance_sheet_data = fetch_balance_sheet_data("INFY", api_key)

# Display the DataFrame
print(balance_sheet_data)


print(balance_sheet_data.columns)

import openpyxl
balance_sheet_data.to_excel('Infosysbalancesheets.xlsx')