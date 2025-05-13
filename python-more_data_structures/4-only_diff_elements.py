#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return_elem = []
    for v1 in set_1: 
        trouve = 0
        for v2 in set_2:
            if v1 == v2: 
                trouve = 1
        if trouve == 0:
            return_elem.append(v1)
    for v1 in set_2: 
        trouve = 0
        for v2 in set_1:
            if v1 == v2: 
                trouve = 1
        if trouve == 0:
            return_elem.append(v1)
    return return_elem
