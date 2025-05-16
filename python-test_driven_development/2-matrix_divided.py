#!/usr/bin/python3
'''
Function that divide a matrix by a number
Return: matrix / div
'''


def matrix_divided(matrix, div):
    '''
    Function that divide a matrix
    '''
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    len_row = 0
    flag_niveau2 = 0
    for row in matrix:
        flag_niveau2 = 1
        new_row_matrix = []
        if len_row != 0 and len_row != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        try:
            len_row = len(row)
        except BaseException:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            flag_niveau2 = 2
            new_row_matrix.append(round(value/div, 2))

        new_matrix.append(new_row_matrix)
    return new_matrix
