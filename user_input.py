from validators import validate_year, validate_phone, validate_first_name, validate_last_name, validate_email, \
    validate_address, validate_author, validate_title, validate_isbn, validate_total_copies


def get_validated_input(prompt, validator):
    while True:
        value = input(prompt)
        try:
            return validator(value)
        except ValueError as error:
            print(error)

def get_isbn():
    return get_validated_input(
        "Enter the ISBN: ",
        validate_isbn
    )


def get_title():
    return get_validated_input(
        "Enter the title: ",
        validate_title
    )


def get_author():
    return get_validated_input(
        "Enter the author",
        validate_author
    )


def get_year():
    return get_validated_input(
        "Enter the year: ",
        validate_year
    )

def get_total_copies():
    return get_validated_input(
        "Enter the total copies: ",
        validate_total_copies
    )


def get_first_name():
    return get_validated_input(
        "Enter the first name: ",
        validate_first_name
    )

def get_last_name():
    return get_validated_input(
        "Enter the last name: ",
        validate_last_name
    )

def get_email():
    return get_validated_input(
        "Enter the email: ",
        validate_email
    )

def get_phone():
    while True:
        return get_validated_input(
            "Enter the phone number: ",
            validate_phone
        )

def get_address():
    return get_validated_input(
        "Enter the address: ",
        validate_address
    )