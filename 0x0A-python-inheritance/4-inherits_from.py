#!/usr/bin/python3
"""
This module defines the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    """
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
