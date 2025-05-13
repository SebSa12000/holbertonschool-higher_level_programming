#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
        matrix (list): A list of lists of integers.

    Returns:
        list: A new matrix with the squared values.
    """
    return [[x ** 2 for x in row] for row in matrix]
