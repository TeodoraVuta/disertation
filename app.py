import streamlit as st
import yfinance as yf

st.write("""
# Hello World!
ola *mami* que ***guapa*** """)

tickerSymbol = "COUR"

tickerData = yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(start='2010-5-31', end='2020-5-31')	

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)