#!/usr/bin/python3
'''
    Class Square 
'''


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):    
    ''' a square class '''
    
    def __init__(self, size):
        ''' initialize the square '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
    
    def __str__(self):
        ret = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return ret
    