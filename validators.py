import re
from datetime import datetime
MIN_YEAR = 1700
MIN_COPIES = 1

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


def validate_isbn(isbn: str) -> bool:
    """
    Automatically detects whether the input is ISBN-10 or ISBN-13
    and validates it according to the corresponding rule.
    """
    cleaned = _clean_isbn(isbn)

    if len(cleaned) == 10:
        return validate_isbn10(isbn)
    elif len(cleaned) == 13:
        return validate_isbn13(isbn)
    else:
        return False

def validate_title(title) -> bool:
    title = title.strip()
    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters long")

    return title

def validate_author(author) -> bool:
    author = author.strip()
    if len(author) < 3:
        raise ValueError("Author must be at least 3 characters long")

    return author

def validate_year(year) -> bool:
    try:
        year = int(year)
    except (ValueError, TypeError):
        return False
    current_year = datetime.now().year
    if year < MIN_YEAR or year > current_year:
        return False

    return True

def validate_total_copies(total_copies) -> bool:
    if isinstance(total_copies, float) and not total_copies.is_integer():
        return False

    if isinstance(total_copies, str) and "." in total_copies:
        return False

    try:
        total_copies = int(total_copies)
    except (ValueError, TypeError):
        return False
    if total_copies < MIN_COPIES:
        return False

    return True













