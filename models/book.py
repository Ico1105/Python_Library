from validators import validate_isbn, _clean_isbn, validate_author, validate_year, validate_total_copies


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

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value.title(value)

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
        if validate_total_copies(value):
            self._total_copies = int(value)
        else:
            raise ValueError(f"Invalid total copies: {value}")








