#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    ret = []
    for i in my_list:
        ret.append(i * number)
    return ret
