#!/usr/bin/python3
for number1 in range(0, 9):
    for number2 in range(number1, 10):
        if number1 == 8 and number2 == 9:
            print("{:01d}{:01d}".format(number1, number2))
        elif number1 != number2:
            print("{:01d}{:01d}".format(number1, number2), end=", ")
