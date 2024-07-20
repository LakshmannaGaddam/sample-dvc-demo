# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = '17SM8GH70SYUPUNI'

from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt


# Initialize SectorPerformances object
sp = SectorPerformances(key=api_key, output_format='pandas')

# Get sector performance data
data, meta_data = sp.get_sector()