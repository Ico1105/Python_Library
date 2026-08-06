from validators import validate_member_id, validate_email, validate_phone, validate_address, \
    validate_first_name, validate_last_name


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
        self._first_name = validate_first_name(value)

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = validate_last_name(value)

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = validate_email(value)

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = validate_phone(value)

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = validate_address(value)
