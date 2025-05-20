#!/usr/bin/python3
'''
Class Square
'''
class Square:
    '''
    Init function and raise error if it's a string or < 0 
    '''
    def __init__(self, size=0):
        self.__size = 0
        if  isinstance(size, str):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    '''
    Function area
    '''
    def area(self):
        return self.__size * self.__size
    
    @property
    def size(self):
        '''Getter to retrieve the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Property setter  to give value to  __size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size
