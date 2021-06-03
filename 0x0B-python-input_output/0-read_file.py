#!usr/bin/python3
"""
This module defines the read_file function
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, mode="r", encoding="utf-8") as fh:
        lines = fh.read()
        print(lines, end="")
