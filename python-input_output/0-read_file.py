#!/usr/bin/python3
'''
    test read file
'''


def read_file(filename=""):
    ''' 
    function to read a file 
    '''
    with open(filename, encoding="utf-8") as file:
        for line in file:
            if line:
                print(line, end="")
            else:
                break
