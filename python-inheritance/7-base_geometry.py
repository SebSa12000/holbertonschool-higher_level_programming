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
        if not type(value) is int:
            msg = name + " must be an integer"
            raise TypeError(msg)
        if value <= 0:
            msg = name + " must be greater than 0"
            raise ValueError(msg)
