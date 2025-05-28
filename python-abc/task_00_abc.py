from abc import ABC, abstractmethod
'''
    class abstract
'''


class Animal(ABC):
    ''' Abstract base class for all animals. '''
    @abstractmethod
    def sound(self):
        ''' Abstract method to be implemented by subclasses. '''
        pass


class Dog(Animal):
    def sound(self):
        ''' Returns the sound made by a dog. '''
        return "Woof!"


class Cat(Animal):
    def sound(self):
        ''' Returns the sound made by a cat. '''
        return "Meow!"
