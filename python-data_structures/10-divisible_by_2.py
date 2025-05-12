def divisible_by_2(my_list=[]):
    new_list = []
    for idx in range(len(my_list)):
        new_list.append(my_list[idx] % 2 == 0)
    return new_list
