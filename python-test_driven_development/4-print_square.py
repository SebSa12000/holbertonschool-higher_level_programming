#!/usr/bin/python3
'''
Function that display a square
Return: None
'''


def print_square(size):
    if not isinstance(size, (float)) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

