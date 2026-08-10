from validators import validate_year, validate_phone, validate_first_name, validate_last_name, validate_email, \
    validate_address


def get_validated_input(prompt, validator):
    while True:
        value = input(prompt)
        try:
            return validator(value)
        except ValueError as error:
            print(error)

def get_isbn():
    return input("Enter the ISBN: ")

def get_title():
    return input("Enter the title: ")

def get_author():
    return input("Enter the author: ")

def get_year():
    while True:
        value = input("Enter the year: ")

        try:
            return validate_year(value)
        except ValueError as error:
            print(error)

def get_total_copies():
    return input("Enter the total copies: ")

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