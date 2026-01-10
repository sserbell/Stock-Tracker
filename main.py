import pandas as pd
import time
from data_fetcher import get_stock_data
import os
"""
Main application entry point.

Handles user input, fetches stock data for single or mutiple tickers, automatically refreshes, and 
writes updated data to a CSV file.    
"""
user_input = input("Please enter one or multiple tickers (comma-separated): ")
file_name = input("Please enter the name for your watchlist: ")
ticker_list = [ticker.strip().upper() for ticker in user_input.split(',')]
previous_data = None # Stores last displayed data

# Handles empty file name input
if file_name.strip() == "":
            file_name = "watchlist"

# Checks whether the CSV file is currently open
file_path = file_name + ".csv"
if os.path.exists(file_path):
    try:
        with open(file_path, "a"):
            pass
    except PermissionError:
        print("Warning: File may be open in another program. Close it to allow updating.")

# Automation section that displays the stock data and refreshes automatically
try:
    while True:
        full_data = []
        
        # Appends all valid ticker information into one single list
        for ticker in ticker_list:
            individual_data = get_stock_data(ticker)
            if individual_data is not None:
                full_data.append(individual_data)
                 
        if not full_data:
            print("No valid stock data found.")
            time.sleep(60)
            continue
        
        # Concatenates all individual DataFrames into one
        final_data = pd.concat(full_data, ignore_index = True)
        # Sorts stocks by percent change
        final_data.sort_values(by="Percent Change", ascending = False, inplace = True)
        
        # Writes the data into a csv file
        try:
            final_data.to_csv(file_name + ".csv", index = False)
        except PermissionError:
            print("Could not update CSV file, file may be open elsewhere.")
        
        # Displays refreshed data only when there is new information, controlled updates
        if previous_data is None or not final_data.equals(previous_data): 
            print(final_data)
            print("CSV file updated.")
            print("\nUpdated at:", time.strftime("%H:%M:%S"))
            previous_data = final_data.copy()
            
        time.sleep(60) # Every 60 seconds
    
except KeyboardInterrupt:
    print("\nStopped price refresh.")
    