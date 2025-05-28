from abc import ABC, abstractmethod
import math

''' class abstract '''


class Shape(ABC):
    ''' init '''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    ''' class circle '''
    def __init__(self, radius):
        self.radius = radius

    ''' class circle '''
    def area(self):
        return math.pi * self.radius * self.radius

    ''' perimeter '''
    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    ''' class rectangle '''
    def __init__(self, width, height):
        self.width = width
        self.height = height

    ''' area of rectangle '''
    def area(self):
        return self.width * self.height

    ''' perimeter '''
    def perimeter(self):
        return self.width * 2 + self.height * 2

''' define the shape info '''
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")