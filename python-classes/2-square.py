#!/usr/bin/python3
'''
Class Square
'''


class Square:
    ''' Init function '''
    def __init__(self, size=0):

        ''' default value + raise exception '''
        self._Square__size = 0
        if isinstance(size, str):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
