#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        prem = 0
        for j in matrix[i]:
            if (prem == 1):
                print(" ", end="")
            else:
                prem = 1
            print("{:d}".format(j), end="")
        print("")
