#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print from.
        x (int): The number of elements to print.

    Returns:
        int: The number of elements printed.
    """
    compteur = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            compteur += 1
        except (ValueError, TypeError):
            continue
    print("")
    return compteur
