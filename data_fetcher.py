import yfinance as yf
import pandas as pd


# Fetch stock data from Yahoo Finance
def get_stock_data(ticker):
    ticker = ticker.strip().upper()

    stock = yf.Ticker(ticker)
    info = stock.info

    current_price = info.get("regularMarketPrice")
    previous_close = info.get("previousClose")

    # Invalid ticker handling
    if not info or current_price is None:
        return None

    price_change = None
    percent_change = None

    if previous_close and previous_close != 0:
        price_change = round(current_price - previous_close, 2)
        percent_change = round((price_change / previous_close) * 100, 2)

    data = {
        "Symbol": info.get("symbol"),
        "Current Price": current_price,
        "Previous Close": previous_close,
        "Market Cap": info.get("marketCap"),
        "Price Change": price_change,
        "Percent Change": percent_change
    }

    return data
