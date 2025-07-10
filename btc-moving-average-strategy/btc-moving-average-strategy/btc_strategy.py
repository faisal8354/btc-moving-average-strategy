import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load some example price data (this is actually Apple, just for demo)
url = "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"
data = pd.read_csv(url)

# Rename columns to make it look more like generic price data
data.rename(columns={"AAPL.Open": "Open", "AAPL.High": "High", 
                     "AAPL.Low": "Low", "AAPL.Close": "Close"}, inplace=True)

# Convert Date to datetime and set index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Simple moving averages
data['SMA20'] = data['Close'].rolling(window=20).mean()
data['SMA50'] = data['Close'].rolling(window=50).mean()

# Generate signals
data['Signal'] = 0
data.loc[20:, 'Signal'] = np.where(data['SMA20'][20:] > data['SMA50'][20:], 1, 0)
data['Position'] = data['Signal'].diff()

# Plot the results
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Close Price', alpha=0.6)
plt.plot(data['SMA20'], label='20-day SMA')
plt.plot(data['SMA50'], label='50-day SMA')

plt.plot(data[data['Position'] == 1].index, 
         data['SMA20'][data['Position'] == 1],
         '^', markersize=10, color='g', label='Buy Signal')

plt.plot(data[data['Position'] == -1].index, 
         data['SMA20'][data['Position'] == -1],
         'v', markersize=10, color='r', label='Sell Signal')

plt.title('Moving Average Crossover Strategy Example')
plt.legend()
plt.grid(True)
plt.show()
