class Rental:
    def __init__(self, rental_id, member_id, isbn, rental_date, due_date, return_date):
        self.rental_id = rental_id
        self.member_id = member_id
        self.isbn = isbn
        self.rental_date = rental_date
        self.due_date = due_date
        self.return_date = return_date


