from datetime import date, timedelta

from json_storage import load_json, save_json
from models.rental import Rental
from constants import RENTAL_PERIOD_DAYS


def generate_rental_id(rentals):
    if not rentals:
        return 1

    return max(rental["rental_id"] for rental in rentals) + 1

def rent_book():
    members = load_json("storage/members.json")
    books = load_json("storage/books.json")
    rentals = load_json("storage/rentals.json")

    # Find member
    for member in members:
        print(
              f"{member['member_id']}."
              f"{member['first_name']} {member['last_name']}"
        )
    member_id = int(input("Enter the member ID: "))
    member = None

    for item in members:
        if item["member_id"] == member_id:
            member = item
            break

    if member is None:
        print("Member not found.")
        return

    # Find books
    for book in books:
        print(
            f"{book['book_id']}."
            f"{book['title']} "
            f"(Available: {book['available_copies']})"
        )
    isbn = input("Enter the book ISBN: ")
    # Fing book
    book = None
    for item in books:
        if item["isbn"] == isbn:
            book = item
            break
    if book is None:
        print("Book not found.")
        return
    # Check availability
    if book["available_copies"] <= 0:
        print("Book is not available.")
        return

    # Create rental
    rental_id = generate_rental_id(rentals)
    rental_date = date.today()
    due_date = rental_date + timedelta(days=RENTAL_PERIOD_DAYS)
    rental = Rental(
        rental_id=rental_id,
        member_id=member_id,
        isbn=isbn,
        rental_date=rental_date.isoformat(),
        due_date=due_date.isoformat(),
        return_date=None,
    )
    book['available_copies'] -= 1
    rentals.append(rental.to_dict())
    save_json("storage/rentals.json", rentals)
    save_json("storage/books.json", books)

    print("Book rented successfully.")

def return_book():
    pass

def show_all_rentals():
    pass

if __name__ == "__main__":
    rent_book()