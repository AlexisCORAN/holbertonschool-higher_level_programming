#!/usr/bin/python3
"""
    This is matrix_divided(matrix, div) module.

    This module defines the division of a new matrix
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix

    Args:
        matrix (int, float): Matrix used to divide.
        div (int, float): Divisor used for the operation.

    Returns:
        (int, float). Return a new divided matrix.
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    size = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if (type(i) is not int and type(i) is not float):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row]for row in (matrix)]
