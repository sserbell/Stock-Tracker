import sqlite3
from datetime import datetime


DATABASE_NAME = "stocks.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            price REAL,
            previous_close REAL,
            market_cap INTEGER,
            price_change REAL,
            percent_change REAL,
            timestamp TEXT
        )
    """)

    connection.commit()
    connection.close()


def insert_stock(stock):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO stocks (
            symbol,
            price,
            previous_close,
            market_cap,
            price_change,
            percent_change,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        stock["Symbol"],
        stock["Current Price"],
        stock["Previous Close"],
        stock["Market Cap"],
        stock["Price Change"],
        stock["Percent Change"],
        datetime.now()
    ))

    connection.commit()
    connection.close()


def get_stock_history(symbol):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM stocks
        WHERE symbol = ?
    """, (symbol,))

    results = cursor.fetchall()

    connection.close()

    return results
