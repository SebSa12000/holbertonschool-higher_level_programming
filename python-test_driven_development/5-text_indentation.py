#!/usr/bin/python3
'''
Function intent text
'''

def text_indentation(text):
    if not isinstance(text, (str)):
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == ':' or i == '?':
            print("")
            print("")
        else:
            print(i, end="")
