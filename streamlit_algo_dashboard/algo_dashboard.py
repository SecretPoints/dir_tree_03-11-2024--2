import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

dates = pd.date_range(start='2023-01-01', periods=100)
index_prices = pd.DataFrame({
    'Date': dates,
    'Index Price': np.random.normal(100, 10, size=(100,))
})

st.title("Algo Trading Dashboard")

st.subheader("Index Prices")
st.line_chart(index_prices.set_index('Date')['Index Price'])

positions = pd.DataFrame({
    'Position': ['AAPL', 'GOOGL', 'TSLA'],
    'Shares': [10, 5, 2],
    'Price': [150, 2700, 700]
})

st.subheader("Current Positions")
st.table(positions)

spot_prices = np.linspace(50, 200, 100)
strike_price = 100
premium = 10

payoff = np.where(spot_prices > strike_price, spot_prices - strike_price - premium, -premium)

fig = go.Figure(data=[go.Scatter(x=spot_prices, y=payoff, mode='lines', name='Payoff')])

fig.update_layout(title='Payoff Graph', xaxis_title='Spot Price', yaxis_title='Payoff')

st.subheader("Payoff Graph")
st.plotly_chart(fig)
payoff = np.where(spot_prices > strike_price, spot_prices - strike_price - premium, -premium)
t(fig)