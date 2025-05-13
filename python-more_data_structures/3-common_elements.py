#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_return = []
    for v1 in set_1:
        for v2 in set_2:
            if v1 == v2:
                list_return.append(v1)
    return list_return
