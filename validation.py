# Small functions to check user input

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter a whole number.")


def get_non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except ValueError:
            print("Invalid input. Enter a whole number.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a value greater than zero.")
        except ValueError:
            print("Invalid input. Enter a number.")
