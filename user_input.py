from validators import validate_year


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