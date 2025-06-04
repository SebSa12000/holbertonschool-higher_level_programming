#!/usr/bin/python3
''' class to json'''


import json


def class_to_json(obj):
    ''' dumps a class '''
    return json.dumps(obj.__dict__)
