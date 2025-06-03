#!/usr/bin/python3
'''
    test write file
'''


def write_file(filename="", text=""):
    '''
        write a file
    '''
    f = open(filename, "w", encoding="utf-8")
    ret = f.write(text)
    f.close()
    return ret
