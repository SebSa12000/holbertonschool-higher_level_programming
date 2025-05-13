#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newl = list(my_list)
    if idx < 0:
        return newl
    if idx >= len(my_list):
        return newl
    newl[idx] = element
    return newl
