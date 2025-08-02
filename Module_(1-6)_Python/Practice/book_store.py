import json
import os

class BookStore:
    def __init__(self):
        self.books = []
        self.file_name = 'books_new.json'
        self.load_books()

    def load_books(self):
        """ Load books from the JSON file. """
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                try:
                    self.books = json.load(file)
                except json.JSONDecodeError:
                    print("Error reading JSON file. Creating a new empty list.")
                    self.books = []
        else:
            print(f"No existing file found. A new file '{self.file_name}' will be created.")

    def save_books(self):
        """ Save books to the JSON file. """
        with open(self.file_name, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        """ Add a new book to the store. """
        title = input("Enter book title: ").strip()
        if not title:
            print("The book title must be a non-empty string.")
            return

        author = input("Enter book author: ").strip()
        if not author:
            print("The book author must be a non-empty string.")
            return

        isbn = input("Enter book ISBN: ").strip()
        if not isbn:
            print("The book ISBN must be a non-empty string.")
            return

        if any(book['isbn'] == isbn for book in self.books):
            print(f"A book with ISBN {isbn} already exists.")
            return

        genre = input("Enter book genre: ").strip()
        if not genre:
            print("The book genre must be a non-empty string.")
            return

        try:
            price = float(input("Enter book price: ").strip())
            if price <= 0:
                print("The price must be a positive number.")
                return
        except ValueError:
            print("The price must be a valid number.")
            return

        try:
            quantity = int(input("Enter quantity in stock: ").strip())
            if quantity < 0:
                print("The quantity must be a non-negative integer.")
                return
        except ValueError:
            print("The quantity must be a valid integer.")
            return

        new_book = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'genre': genre,
            'price': price,
            'quantity': quantity
        }
        self.books.append(new_book)
        self.save_books()
        print("Book added successfully.")

    def view_books(self):
        """ View all books in the store. """
        if not self.books:
            print("No books available.")
            return

        print("\n===== List of Books =====")
        for index, book in enumerate(self.books, start=1):
            print(f"""
Book No: {index}
Title   : {book['title']}
Author  : {book['author']}
ISBN    : {book['isbn']}
Genre   : {book['genre']}
Price   : tk {book['price']}
Quantity: {book['quantity']}
-------------------------------
            """)

    def search_book(self):
        """ Search for a book by ISBN. """
        isbn = input("Enter book ISBN to search: ").strip()
        for book in self.books:
            if book['isbn'] == isbn:
                print(f"""
Found Book:
Title   : {book['title']}
Author  : {book['author']}
ISBN    : {book['isbn']}
Genre   : {book['genre']}
Price   : tk {book['price']}
Quantity: {book['quantity']}
                """)
                return
        print(f"No book found with ISBN {isbn}")

    def remove_book(self):
        """ Remove a book by ISBN. """
        isbn = input("Enter book ISBN to remove: ").strip()
        for book in self.books:
            if book['isbn'] == isbn:
                self.books.remove(book)
                self.save_books()
                print("Book removed successfully.")
                return
        print(f"No book found with ISBN {isbn}")