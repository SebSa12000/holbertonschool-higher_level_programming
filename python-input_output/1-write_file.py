#!/usr/bin/python3
'''
    test write file
'''


def write_file(filename="", text=""):
    '''
        write a file
    '''
    with open(filename, "w", encoding="utf-8") as f:
        ret = f.write(text)
        f.close()
        return ret
