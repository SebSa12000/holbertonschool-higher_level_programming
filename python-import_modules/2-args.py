#!/usr/bin/python3
import sys
args = sys.argv[1:]
if len(args) == 0:
    print("0 arguments.")
elif len(args) > 0:
    print("{} arguments:".format(len(args)))
    for i, arg in enumerate(args):
        print("{}: {}".format(i + 1, arg))
