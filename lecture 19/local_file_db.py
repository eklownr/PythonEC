import json


class BookDatabase:
    def __init__(self, filename="book_inventory.json"):
        self.filename = filename
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.books, file, indent=2)

    def add_book(self, title, author, price):
        book = {"title": title, "author": author, "price": price}
        self.books.append(book)
        self.save_data()

    def get_all_books(self):
        return self.books


book_db = BookDatabase()

book_db.add_book("Python for Beginners", "John Doe", 29.99)
book_db.add_book("Database Design 101", "Jane Smith", 39.99)

all_books = book_db.get_all_books()

for book in all_books:
    print(f"Title: {book['title']}, Author: {book['author']}, Price: ${book['price']}")
