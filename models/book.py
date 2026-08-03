from validators import validate_isbn, _clean_isbn


class Book:
    def __init__(self, isbn, title, author, year, total_copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.total_copies = total_copies

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        cleaned = _clean_isbn(value)

        if not validate_isbn(cleaned):
            raise ValueError("Invalid ISBN")

        self._isbn = cleaned







