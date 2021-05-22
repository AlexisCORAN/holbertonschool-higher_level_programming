#!/usr/bin/python3
"""
    This is say_my_name(first_name, last_name="") module.

    This module defines a first and last name.
"""


def say_my_name(first_name, last_name=""):
    """ This function print a first and last name

    Args:
        first_name (str): first parameter.
        last_name (str): second parameter.

    Returns:
       The return value. A string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
