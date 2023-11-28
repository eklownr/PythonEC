import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()  # This is used to interact with the database

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        price REAL
    )
"""
)

cursor.execute(
    "INSERT INTO books (title, author, price) VALUES (?, ?, ?)",
    ("Python for Beginners", "John Doe", 29.99),
)
cursor.execute(
    "INSERT INTO books (title, author, price) VALUES (?, ?, ?)",
    ("Database Design 101", "Jane Smith", 39.99),
)

conn.commit()
conn.close()
