#!/usr/bin/python3
"""Defines a class Square"""


class Square:
     """A class named Square
    Attributes:
    __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """
        Args:
            size (int): size for  attribute of class instance
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2