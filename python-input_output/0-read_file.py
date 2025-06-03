#!/usr/bin/python3
'''
    test read file
'''


def read_file(filename=""):
    ''' function to read a file '''
    with open(filename,"r") as file:
        contents = file.read()
        print(contents)
