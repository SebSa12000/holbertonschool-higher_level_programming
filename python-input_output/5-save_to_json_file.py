#!/usr/bin/python3
''' save a json object in a file '''


import json


def save_to_json_file(my_obj, filename):
    ''' save a json object in a file '''
    with open(filename, "w", encoding="utf-8") as f:
        data = json.dumps(my_obj)
        f.write(data)
