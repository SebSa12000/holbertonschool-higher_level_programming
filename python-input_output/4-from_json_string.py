#!/usr/bin/python3
''' Serialise a string in json'''


import json


def from_json_string(my_str):
    '''Serialise a string in json'''
    return json.loads(my_str)
