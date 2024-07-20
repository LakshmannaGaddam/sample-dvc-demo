import requests
import pandas as pd

# Your Alpha Vantage API key
api_key = '17SM8GH70SYUPUNI'

def fetch_sector_performance(api_key):
    url = f"https://www.alphavantage.co/query?function=SECTOR&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    sector_performance = pd.DataFrame(data['Rank A: Realtime Performance']).T
    sector_performance.columns = ['Performance']
    return sector_performance

def fetch_industry_performance(api_key, sector):
    url = f"https://www.alphavantage.co/query?function=SECTOR&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    industry_performance = pd.DataFrame(data[f'Rank D: {sector}']).T
    industry_performance.columns = ['Performance']
    return industry_performance

# Fetch sector performance data
sector_performance_data = fetch_sector_performance(api_key)

url = f"https://www.alphavantage.co/query?function=SECTOR&apikey={api_key}"
response = requests.get(url)
data = response.json()
print(data)
# Analyze sector performance
print("Sector Performance:")
print(sector_performance_data)

# Choose a sector (e.g., 'Technology')
sector = 'Technology'

# Fetch industry performance data for the chosen sector
industry_performance_data = fetch_industry_performance(api_key, sector)

# Analyze industry performance
print(f"\nIndustry Performance for {sector}:")
print(industry_performance_data)
