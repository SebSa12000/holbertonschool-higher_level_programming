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
        with open(filename) as f:
            pickle.dump(self, f)

    @classmethod 
    def deserialize(cls, filename):
        with open(filename) as f:
            self = pickle.load(f)
