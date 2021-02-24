''' the goal will be to create a program that allows us to pass different
stock trading strategies to backtest it to see how it would have performed
within the last year, two years, etc. '''

# retrieve data -> using yfinance to retrieve minute data on stock for last 2 months
# test strategy
# return profit / loss from strategy

'''Only 7 days worth of 1m granularity data are allowed to be fetched per request.'''

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go

msft = yf.Ticker("MSFT")

# retrieving stock data every minute for the last 7 days
df = msft.history(period="7d", interval="1m")

# // below code is for graphing the data
# creating trace - setting data for each point on the candlestick
trace1 = {
    'x': df.index,
    'open': df.Open,
    'close': df.Close,
    'high': df.High,
    'low': df.Low,
    'type': 'candlestick',
    'name': 'MSFT',
    'showlegend': True
}

data = [trace1]

# creating layout for the graph
layout = go.Layout({
    'title': {
        'text': 'Microsoft(MSFT) - Intraday Data For Last 7 Open Market Days',
        'font': {
            'size': 15
        }
    }
})

# graphing the data
fig = go.Figure(data=data, layout=layout)
fig.write_html("Microsoft(MSFT) - Intraday Data For Last 7 Open Market Days.html")
fig.show()
