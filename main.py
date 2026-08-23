from services.book_service import add_book, edit_book
from services.member_service import add_member, edit_member
from services.rental_service import rent_book, return_book, show_all_rentals


def main():
    while True:
        print("=== LIBRARY ===")
        print("1. Books")
        print("2. Members")
        print("3. Rentals")
        print("0. Exit")

        choice = int(input("Enter your choice: "))
        print()

        if choice == 1:
            books_menu()

        elif choice == 2:
            members_menu()

        elif choice == 3:
            rentals_menu()

        elif choice == 0:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def books_menu():
    while True:
        print("\n=== BOOKS ===")
        print("1. Add book")
        print("2. Edit book")
        print("3. List book")
        print("0. Back")

        choice = int(input("Enter your choice: "))
        print()

        if choice == 1:
            add_book()
        elif choice == 2:
            edit_book()
        elif choice == 3:
            pass
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please try again.")

def members_menu():
    while True:
        print("\n=== MEMBERS ===")
        print("1. Add member")
        print("2. Edit member")
        print("3. List member")
        print("0. Back")
        choice = int(input("Enter your choice: "))
        print()

        if choice == 1:
            add_member()
        elif choice == 2:
            edit_member()
        elif choice == 3:
            pass
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please try again.")

def rentals_menu():
    while True:
        print("\n=== RENTALS ===")
        print("1. Add rental")
        print("2. Return rental")
        print("3. List rental")
        print("0. Back")

        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            rent_book()
        elif choice == 2:
            return_book()
        elif choice == 3:
            show_all_rentals()
        elif choice == 0:
            pass
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()