#!/usr/bin/python3
"""
This module defines the pascal_triangle function
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal’s triangle of (n)
    """
    if n <= 0:
        return []
    else:
