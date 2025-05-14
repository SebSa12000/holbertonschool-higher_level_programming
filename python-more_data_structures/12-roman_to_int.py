#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    precedent = ''
    if isinstance(roman_string, str):
        for character in roman_string:
            if character == 'I':
                sum = sum + 1
            elif character == 'V':
                if precedent == 'I':
                    sum = sum - 2
                sum = sum + 5
            elif character == 'X':
                if precedent == 'I':
                    sum = sum - 2
                sum = sum + 10
            elif character == 'L':
                sum = sum + 50
            elif character == 'C':
                if precedent == 'X':
                    sum = sum - 20
                sum = sum + 100
            elif character == 'D': 
                sum = sum + 500
            precedent = character
    return sum
