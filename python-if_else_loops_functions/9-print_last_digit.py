def print_last_digit(number):
    # Print the last digit of a number and return it.
    if number < 0:
        number = -number
    last_digit = number % 10
    print(last_digit, end="")
    return last_digit