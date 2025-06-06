#!/usr/bin/python3
''' Adds all arguments to a python list and
    save them to a file'''


import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:

    obj = load_from_json_file("add_item.json")
except BaseException:
    obj = []

for i in sys.argv[1:]:
    obj.append(i)
save_to_json_file(obj, "add_item.json")
