def element_at(my_list, idx, element):
    # replace an element of a list
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list