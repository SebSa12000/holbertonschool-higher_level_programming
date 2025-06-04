#!/usr/bin/python3
''' return class dict'''


def class_to_json(obj):
    ''' dumps a class '''
    return obj.__dict__
