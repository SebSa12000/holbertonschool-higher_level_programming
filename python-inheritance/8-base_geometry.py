#!/usr/bin/python3
'''
base geometry
'''


class BaseGeometry:
    ''' a basic class '''
    def area(self):
        raise Exception("area() is not implemented")
    
    @classmethod
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            msg = name + " must be an integer"
            raise TypeError(msg)
        if value <= 0:
            msg = name + " must be greater than 0"
            raise ValueError(msg)

class Rectangle(BaseGeometry):
    ''' class rectangle '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
