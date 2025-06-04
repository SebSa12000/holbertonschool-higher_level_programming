#!/usr/bin/python3
''' load json from a file '''


import json


def load_from_json_file(filename):
    ''' load json from a file '''
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
