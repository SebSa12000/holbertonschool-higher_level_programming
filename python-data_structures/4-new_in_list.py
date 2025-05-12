#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = list(my_list)
    if idx < 0:
        return None
    if idx >= len(newlist):
        return None
    newlist[idx] = element
    return newlist
