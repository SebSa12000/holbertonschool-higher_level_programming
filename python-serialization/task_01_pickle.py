#!/usr/bin/python3
''' custom object'''


import pickle


def CustomObject():
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        ''' serialize the file '''
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        ''' deserialize the file '''
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            return None
