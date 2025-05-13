#!/usr/bin/python3
def uniq_add(my_list=[]):
    int_trouve = []
    sum = 0
    for i in range(len(my_list)):
        trouve = 0
        for j in int_trouve:
            if j == my_list[i]:
                trouve = 1
        if trouve == 0:
            int_trouve.append(my_list[i])
            sum = sum + my_list[i]
    return sum
