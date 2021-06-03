#!/usr/bin/python3
"""
This module defines the append_write function
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as fh:
        append_file = fh.write(text)
    return (append_file)
