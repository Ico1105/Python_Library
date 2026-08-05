from validators import validate_member_id, validate_name


class Member:
    def __init__(self, member_id, first_name, last_name, email, phone, address):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        if validate_member_id(value):
            self._member_id = int(value)
        else:
            raise ValueError(f"Invalid member ID: {value}")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if validate_name(value):
            self._first_name = value.strip()