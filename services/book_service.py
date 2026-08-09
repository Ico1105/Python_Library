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
    isbn = get_isbn()
    title = get_title()
    author = get_author()
    year = get_year()
    total_copies = get_total_copies()

    book = Book(isbn=isbn,
                title=title,
                author=author,
                year=year,
                total_copies=total_copies,
                )


    books = load_json("books.json")
    books.append(book.to_dict())
    save_json("books.json", books)

