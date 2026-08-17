import re
from datetime import datetime
MIN_YEAR = 1700
MIN_COPIES = 1
MIN_MEMBER_ID = 0

def _clean_isbn(isbn):
    return re.sub(r'[-\s]', '', isbn)

def validate_isbn10(isbn: str) -> bool:
    """
    Validates an ISBN-10 code.
    Format: 9 digits + (digit or 'X' representing 10)
    Rule: sum(digit_i * (10 - i)) must be divisible by 11, i=0..9
    """
    isbn = _clean_isbn(isbn).upper()

    if len(isbn) != 10:
        return False

    if not isbn[:9].isdigit():
        return False

    if not (isbn[9].isdigit() or isbn[9] == 'X'):
        return False

    total = 0
    for i, char in enumerate(isbn):
        value = 10 if char == 'X' else int(char)
        total += value * (10 - i)

    return total % 11 == 0


def validate_isbn13(isbn: str) -> bool:
    """
    Validates an ISBN-13 code.
    Format: 13 digits
    Rule: alternating weights of 1 and 3, sum must be divisible by 10.
    """
    isbn = _clean_isbn(isbn)

    if len(isbn) != 13 or not isbn.isdigit():
        return False

    total = 0
    for i, char in enumerate(isbn):
        weight = 1 if i % 2 == 0 else 3
        total += int(char) * weight

    return total % 10 == 0


def validate_isbn(isbn):
    """
    Automatically detects whether the input is ISBN-10 or ISBN-13
    and validates it according to the corresponding rule.
    """
    cleaned = _clean_isbn(isbn)

    if len(cleaned) == 10:
        if not validate_isbn10(cleaned):
            raise ValueError("Invalid ISBN-10")
    elif len(cleaned) == 13:
        if not validate_isbn13(cleaned):
            raise ValueError("Invalid ISBN-13")
    else:
        raise ValueError("ISBN must contain 10 of 13 characters")

    return cleaned.upper()

def validate_title(title) -> bool:
    title = title.strip()
    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters long")

    return title.title()

def validate_author(author) -> bool:
    author = author.strip()
    if len(author) < 3:
        raise ValueError("Author must be at least 3 characters long")

    return author.title()

def validate_year(year) -> int:
    try:
        year = int(year)
    except (ValueError, TypeError):
        raise ValueError("Year must be an integer")

    current_year = datetime.now().year

    if year < MIN_YEAR or year > current_year:
        raise ValueError("Invalid year.")

    return year

def validate_total_copies(value):
    try:
        value = int(value)
    except:
        raise ValueError(f"Total copies must be an integer {value}")
    return value

def validate_available_copies(value, total_copies):
    try:
        value = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"Available copies must be an integer")
    if value < 0:
        raise ValueError("Available copies must be an integer.")

    if value > total_copies:
        raise ValueError("Available copies must be less than or equal to total copies.")

    return value
def validate_member_id(member_id) -> int:
    try:
        member_id = int(member_id)
    except:
        raise (ValueError(f"Invalid member ID: {member_id}"))
    if member_id < MIN_MEMBER_ID:
        raise ValueError("Member ID must be greater than or equal to 0.")
    return member_id


def validate_first_name(first_name) -> bool:
    first_name = first_name.strip()

    if len(first_name) < 3:
        raise ValueError("Name must be at least 3 characters long")
    return first_name.title()

def validate_last_name(last_name) -> bool:
    last_name = last_name.strip()

    if len(last_name) < 3:
        raise ValueError("Name must be at least 3 characters long")
    return last_name.title()

def validate_email(email) -> bool:
    email = email.strip()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format")
    return email

def validate_phone(phone: str):
    phone = phone.strip()
    if not re.match(r"^\d{10}$", phone):
        raise ValueError("Invalid phone number format")
    return phone

def validate_address(address: str):
    address = address.strip()
    if len(address) < 5:
        raise ValueError("Address must be at least 5 characters long")

    return address.title()












