#!/usr/bin/python3
''' convert csv in json '''


import csv
import json


def convert_csv_to_json(filename):
    ''' convert csv in json '''
    try:
        with open(filename, "r") as csv_file:
            csv_file = csv.DictReader(csv_file)
            data = list(csv_file)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True

    except FileNotFoundError:
        return False
