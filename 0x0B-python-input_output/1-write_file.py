#!/usr/bin/python3
"""
This module defines the write_file funciton
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and 
    returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as fh:
        add_write = fh.write(text)
    return (add_write)
