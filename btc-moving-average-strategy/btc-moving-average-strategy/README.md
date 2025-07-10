# Moving Average Crossover Strategy (Sample)

This is a small Python project to test out a simple moving average crossover strategy 
on price data. Right now it's using sample Apple stock data as a stand-in for BTC.

## What it does
- Calculates 20-day and 50-day simple moving averages on the close price.
- Generates buy/sell signals when the short SMA crosses the long SMA.
- Plots the results with entry/exit points.

## To run
Install the dependencies first:

```
pip install -r requirements.txt
```

Then run the script:

```
python btc_strategy.py
```

## Note
This is a simple test example, mainly to practice pandas and matplotlib. 
In future, I plan to connect this to real BTC/ETH data from an API.
