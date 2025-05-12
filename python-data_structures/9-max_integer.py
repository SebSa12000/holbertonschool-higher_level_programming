#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = my_list[0]
    for idx in range(1, len(my_list)):
        if max < my_list[idx]:
            max = my_list[idx]
    return max
