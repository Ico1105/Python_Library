from validators import validate_year

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
    return input("Enter the first name: ")

def get_last_name():
    return input("Enter the last name: ")

def get_email():
    return input("Enter the email: ")

def get_phone():
    return input("Enter the phone number: ")

def get_address():
    return input("Enter the address: ")