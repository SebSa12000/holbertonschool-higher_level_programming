#!/usr/bin/python3
def safe_print_division(a, b):
    # division by zero
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        # if no error
        print("Inside result: {}".format(result))
    return result
