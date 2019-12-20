# -*- coding: utf-8 -*-
"""
"""

# TODO: Make own candlestick output generator with matplotlib

#import plotly.graph_objects as go
from plotly import graph_objs as go
import pandas as pd
from datetime import datetime

df = pd.read_csv('AAPL.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Datetime'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.show()
