#!/usr/bin/python3
'''
Class Square
'''


class Square:
    '''
    Init function and raise error if it's a string or < 0
    '''
    def __init__(self, size=0):
        ''' initialize and raise error if needed '''
        self._Square__size = 0
        if isinstance(size, str):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    '''
    Function area
    '''
    def area(self):
        ''' return the ² of the size'''
        return self._Square__size * self._Square__size
