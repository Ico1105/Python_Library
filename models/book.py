from validators import validate_isbn, _clean_isbn, validate_author, validate_year, validate_total_copies, validate_title

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
        self._isbn = validate_isbn(value)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = validate_title(value)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = validate_author(value)

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = validate_year(value)

    @property
    def total_copies(self):
        return self._total_copies

    @total_copies.setter
    def total_copies(self, value):
            self._total_copies = validate_total_copies(value)

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "total_copies": self.total_copies,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            isbn=data["isbn"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            total_copies=data["total_copies"],
        )









