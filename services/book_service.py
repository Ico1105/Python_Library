from json_storage import load_json, save_json
from models.book import Book
from user_input import (
    get_isbn,
    get_title,
    get_author,
    get_year,
    get_total_copies,
)

def add_book():
    books = load_json("storage/books.json")

    isbn = get_isbn()
    if isbn is None:
        print("Cancelled.")
        return

    title = get_title()
    if title is None:
        print("Cancelled.")
        return

    author = get_author()
    if author is None:
        print("Cancelled.")
        return

    year = get_year()
    if year is None:
        print("Cancelled.")
        return

    total_copies = get_total_copies()
    if total_copies is None:
        print("Cancelled.")
        return

    book = Book(isbn=isbn,
                title=title,
                author=author,
                year=year,
                total_copies=total_copies,
    )


    books.append(book.to_dict())
    save_json("storage/books.json", books)

def edit_book():
    books = load_json("storage/books.json")
    for book in books:
        print(f"{book['isbn']}. {book['title']} by {book['author']}")
    book_isbn = input("Enter the book ISBN to edit: ")
    for book in books:
        if book["isbn"] == book_isbn:
            fields = {k: v for k, v in book.items() if k != "isbn"}
            for i, (k, v) in enumerate(fields.items(), start=1):
                print(f"{i}. {k}: {v}")
            choice = int(input("Enter the field you want to edit: "))
            edit_function = {
                "title": get_title,
                "author": get_author,
                "year": get_year,
                "total_copies": get_total_copies,
            }
            field = list(fields.keys())[choice - 1]
            get_value = edit_function[field]
            new_value = get_value()
            book[field] = new_value
            save_json("storage/books.json", books)
            print("=" * 20)

def show_all_books():
    books = load_json("storage/books.json")
    for book in books:
        print(f"ISBN: {book['isbn']}. \n"
              f"Title: {book['title']} \n"
              f"Author: {book['author']}\n"
              f"Year: {book['year']}\n"
              f"Total Copies: {book['total_copies']}\n"
              f"Available Copies: {book['available_copies']}\n")
        print("=" * 20)

def delete_book():
    books = load_json("storage/books.json")
    archive = load_json("storage/archived_books.json")
    rentals = load_json("storage/rentals.json")
    for book in books:
        print(f"{book['isbn']}."
              f"{book['title']}"
              f"{book['author']}")
    book_isbn = input("Enter the book ISBN to delete: ")

    for rental in rentals:
        if rental['isbn'] == book_isbn and rental['return_date'] is None:
            print("Book is currently rented. Please return the book first.")
            print("Book cannot be deleted.")
            return

    for book in books:
        if book["isbn"] == book_isbn:
            archive.append(book)
            books.remove(book)
            save_json("storage/books.json", books)
            save_json("storage/archive_books.json", archive)
            print("Book deleted successfully.")
            return

def restore_book():
    archive = load_json("storage/archive_books.json")
    books = load_json("storage/books.json")
    for book in archive:
        print(f"{book['isbn']}."
              f"{book['title']}"
              f"{book['author']}")
    book_isbn = input("Enter the book ISBN to restore: ")
    for book in archive:
        if book["isbn"] == book_isbn:
            books.append(book)
            archive.remove(book)
            save_json("storage/books.json", books)
            save_json("storage/archive_books.json", archive)
            print("Book restored successfully.")
            return
    print("Book not found in archive.")

def list_archived_books():
    archive = load_json("storage/archive_books.json")
    if not archive:
        print("No archived books found.")
        return
    print("ARCHIVED BOOKS:")
    for book in archive:
        print(f"ISBN -> {book['isbn']}\n"
              f"Title: {book['title']}\n"
              f"Author: {book['author']}")
        print("=" * 20)




if __name__ == "__main__":
    edit_book()