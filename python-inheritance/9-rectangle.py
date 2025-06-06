#!/usr/bin/python3
'''
    Class Rectangle
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' a rectangle class '''

    def __init__(self, width, height):
        ''' initialize the rectangle '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        ret = "[Rectange] " + str(self.__width) + "/" + str(self.__height)
        return ret
