import time

from data_fetcher import get_stock_data
from database import create_database, insert_stock


"""
Main application entry point.

Fetches stock data from Yahoo Finance,
stores historical data in SQLite,
and refreshes automatically.
"""


# Create database when program starts
create_database()


user_input = input(
    "Please enter one or multiple tickers (comma-separated): "
)


ticker_list = [
    ticker.strip().upper()
    for ticker in user_input.split(',')
]


previous_data = {}


try:

    while True:

        current_data = {}

        for ticker in ticker_list:

            stock_data = get_stock_data(ticker)

            if stock_data is not None:

                current_data[ticker] = stock_data

                # Store in database
                insert_stock(stock_data)


        if not current_data:
            print("No valid stock data found.")

        else:

            # Only display changes
            if current_data != previous_data:

                print("\nUpdated Stock Data:")

                for ticker, data in current_data.items():

                    print("--------------------------------")
                    print("Symbol:", data["Symbol"])
                    print("Price:", data["Current Price"])
                    print("Change:", data["Price Change"])
                    print("% Change:", data["Percent Change"])

                print(
                    "\nUpdated at:",
                    time.strftime("%H:%M:%S")
                )

                previous_data = current_data.copy()


        # Refresh every minute
        time.sleep(60)


except KeyboardInterrupt:

    print("\nStopped price refresh.")
