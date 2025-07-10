# Moving Average Crossover Strategy (Sample)

This is a small Python project I built to test a simple moving average crossover strategy on price data.  
It uses sample Apple stock data as a stand-in for BTC prices, mainly to practice time-series analysis and generating basic buy/sell signals.

## What it does
- Calculates 20-day and 50-day simple moving averages on close prices.
- Generates buy and sell signals when the short SMA crosses the long SMA.
- Plots the results, showing close prices, SMAs, and the entry/exit points.

## How to run
Install the dependencies first:

    pip install -r requirements.txt

Then run the script:

    python btc_strategy.py

A plot will pop up showing the strategy signals on top of the price chart.

## Note
This is mainly a practice project to explore pandas, numpy, and matplotlib on financial time-series data.  
In future, I plan to replace the sample CSV with live BTC/ETH data from an API.
