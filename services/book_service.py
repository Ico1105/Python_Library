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

def delete_book():
    pass


if __name__ == "__main__":
    edit_book()