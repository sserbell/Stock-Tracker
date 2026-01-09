# 📈 Stock-Tracker
A Python-based stock tracker that fetches real-time market data and displays meaningful stock information while storing the information in a CSV file.

---

## 🚀 Features
- Fetches live stock data from the Yahoo Finance API
- Displays:
    - Stock symbol
    - Current price
    - Price change
    - Percent change
    - Previous close
    - Market capitalization
- Supports multiple tickers at once
- Refreshes data automatically while running
- Updates the CSV file only when changes occur
- Sorts stocks by percent change

---

## 🛠 Tech Stack:
- **Language:** Python
- **Data Analysis:** Pandas
- **Financial Data:** Yahoo Finance API (`yfinance`)
- **Data Storage:** CSV
- **Interface:** Terminal/ Command Line

---

How to run:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-tracker.git
   cd stock-tracker
2. Install dependencies:
   ```bash
   pip install pandas yfinance
3. Run the program:
   ```bash
   python main.py
4. Enter:
   - One or more stock tickers (comma-separated)
   - A file name for your CSV file  
The program will continue running and automatically refresh the stock data. Updates are displayed and updated in the terminal and CSV file only when a change occurs.  
⚠️ The CSV file must be closed while the program is running to update.  

---

## 📊 Sample Output:
<img width="1041" height="205" alt="image" src="https://github.com/user-attachments/assets/d991e99a-8174-4631-9a8f-e47fce36e37f" />

---

## 📚 Knowledge Gained:
- Learned to integrate and work with a financial data API
- Processed and analyzed market data using Pandas
- Built a continuously running Python program with controlled updates
- Improved understanding of data comparison, file handling, and automation
