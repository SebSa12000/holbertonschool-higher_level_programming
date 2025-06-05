#!/usr/bin/python3
''' class student '''


class Student():
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' return dict representation of the class '''
        return self.__dict__
