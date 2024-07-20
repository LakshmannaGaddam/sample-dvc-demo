import pandas as pd
import matplotlib.pyplot as plt
import requests

# Your Alpha Vantage API key
api_key = '17SM8GH70SYUPUNI'

def fetch_balance_sheet_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    balance_sheet = pd.DataFrame(data['annualReports']).set_index('fiscalDateEnding')
    return balance_sheet

def comparative_analysis(balance_sheets):
    for year, df in balance_sheets.items():
        print(f"\nComparative Analysis for {year}:\n")
        print(df)

def common_size_analysis(balance_sheets):
    for year, df in balance_sheets.items():
        total_assets = df.loc['totalAssets']
        common_size = df / total_assets * 100
        print(f"\nCommon Size Analysis for {year}:\n")
        print(common_size)

def plot_common_size_analysis(balance_sheets):
    fig, axs = plt.subplots(len(balance_sheets), 1, figsize=(10, 6*len(balance_sheets)))
    for i, (year, df) in enumerate(balance_sheets.items()):
        total_assets = df.loc['totalAssets']
        common_size = df / total_assets * 100
        ax = axs[i]
        ax.set_title(f"Common Size Analysis for {year}")
        common_size.T.plot(kind="bar", ax=ax)
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.show()

symbol = 'INFY'
years = [2020, 2021, 2022]  # Years for which you want to fetch data

balance_sheets = {}
for year in years:
    balance_sheet_data = fetch_balance_sheet_data(symbol, api_key)
    balance_sheets[year] = balance_sheet_data



comparative_analysis(balance_sheets)
common_size_analysis(balance_sheets)
plot_common_size_analysis(balance_sheets)


print(balance_sheets.items())