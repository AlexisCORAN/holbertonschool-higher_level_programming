#!/usr/bin/python3
"""
This module defines the Base class
"""


class Base:
    """Representation of Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
