#!/usr/bin/python3
"""
    This is print_square(size) module.

    This module defines a size for print a square
"""


def print_square(size):
    """ Print a square with the character "#"

    Args:
        size (int): size length of the square

    Returns:
        The return value. Print a square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size > 0:
        for row in range(size):
            for column in range(size):
                print("#", end="")
            print()
