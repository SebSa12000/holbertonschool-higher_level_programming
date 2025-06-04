#!/usr/bin/python3
'''
    test append file
'''


def append_write(filename="", text=""):
    '''
        append a file
    '''
    with open(filename, "a", encoding="utf-8") as f:
        ret = f.write(text)
        f.close()
        return ret
