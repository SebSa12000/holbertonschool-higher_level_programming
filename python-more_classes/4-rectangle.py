#!/usr/bin/python3
'''
Class Rectangle
'''


class Rectangle:
    '''
    Init function and raise error if it's a string or < 0
    '''
    def __init__(self, width=0, height=0):
        self._Rectangle__width = 0
        self._Rectangle__height = 0
        if isinstance(width, str):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if isinstance(height, str):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        '''Getter to retrieve the width'''
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        '''Property setter  to give value to  width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value
        return self._Rectangle__width

    @property
    def height(self):
        '''Getter to retrieve the height'''
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        '''Property setter  to give value to  height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
        return self._Rectangle__height

    def area(self):
        ''' return the area '''
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        ''' return the perimeter '''
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0
        else:
            return self._Rectangle__height * 2 + self._Rectangle__width * 2

    def print(self):
        ''' print rectangle '''
        new_string = ""
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            new_string = ""
            print(new_string)
        else:
            for i in range(self._Rectangle__height):
                for j in range(self._Rectangle__width):
                    new_string = new_string + "#"
                new_string = new_string + "\n"
            print(new_string, end="")

    def __str__(self):
        ''' print rectangle '''
        new_string = ""
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            new_string = ""
            return new_string
        else:
            for i in range(self._Rectangle__height):
                for j in range(self._Rectangle__width):
                    new_string = new_string + "#"
                new_string = new_string + "\n"
            return new_string[:-1]
        
    def __repr__(self):
        ''' print rectangle '''
        new_string = "Rectangle(" + str(self._Rectangle__width) + "," + str(self._Rectangle__height) + ")"
        return new_string
