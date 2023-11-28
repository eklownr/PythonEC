import sqlite3

connection = sqlite3.connect("my_cat.db")
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS cats (
        id INTEGER PRIMARY KEY,
        catname TEXT,
        furcolor TEXT
    )
"""
)

cursor.execute(
    "INSERT INTO cats (catname, furcolor) VALUES (?, ?)",
    ("Charlie", "orange"),
)

connection.commit()
connection.close()
