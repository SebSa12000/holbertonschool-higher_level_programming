#!/usr/bin/python3
import json
'''
    serialization
'''


def serialize_and_save_to_file(data, filename):
    ''' serialize '''
    json.dump(data,filename)

def load_and_deserialize(filename):
    ''' deserialize '''
    return json.load(filename)
