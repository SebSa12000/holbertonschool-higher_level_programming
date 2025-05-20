#!/usr/bin/python3
'''
Class Square
'''


class Square:
    '''
    Init function and raise error if it's a string or < 0
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = 0
        self.__position = (0, 0)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''Getter to retrieve the position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Property setter  to give value to  __position'''
        if not isinstance(value, tuple):
            raise TypeError("sposition must be a tuple of 2 positive integers")
        self.__position = value
        return self.__position

    def my_print(self):
        '''Print a square with #'''
        if self.size > 0:
            x, y = self.__position
            for i in range(self.size):
                for k in range(x):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
        else:
            print("")
