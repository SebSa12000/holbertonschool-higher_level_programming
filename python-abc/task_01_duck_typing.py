from abc import ABC, abstractmethod

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
        return 3.14159 * self.radius * self.radius

    ''' perimeter '''
    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    ''' class rectangle '''
    def __init__(self, longueur, largeur):
        self.width = largeur
        self.height = longueur

    ''' area of rectangle '''
    def area(self):
        return self.width * self.height

    ''' perimeter '''
    def perimeter(self):
        return self.width * 2 + self.height * 2
