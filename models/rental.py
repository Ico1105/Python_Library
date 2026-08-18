class Rental:
    def __init__(self, rental_id, member_id, isbn, rental_date, due_date, return_date):
        self.rental_id = rental_id
        self.member_id = member_id
        self.isbn = isbn
        self.rental_date = rental_date
        self.due_date = due_date
        self.return_date = return_date


    def to_dict(self):
        return {
            "rental_id": self.rental_id,
            "member_id": self.member_id,
            "isbn": self.isbn,
            "rental_date": self.rental_date,
            "due_date": self.due_date,
            "return_date": self.return_date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            rental_id=data["rental_id"],
            member_id=data["member_id"],
            isbn=data["isbn"],
            rental_date=data["rental_date"],
            due_date=data["due_date"],
            return_date=data["return_date"],
        )
