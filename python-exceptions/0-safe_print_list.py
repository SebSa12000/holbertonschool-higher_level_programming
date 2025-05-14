#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    compteur = 0
    for val in my_list:
        try:
            if compteur < x:
                print(val, end="")
                compteur = compteur + 1
        except:
            print("", end="")
    print("")
    return compteur
