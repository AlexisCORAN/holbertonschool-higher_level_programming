#!/usr/bin/python3
"""
This module defines the BaseGeometry class
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
