#!/usr/bin/python3
"""
This module defines the MyInt class
"""


class MyInt(int):
    """
    A class named MyInt
    """

    def __eq__(self, other):
        """Swaps the eq builtin"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Swaps the ne builtin"""
        return int.__eq__(self, other)
