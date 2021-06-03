#!usr/bin/python3
"""
This module defines the read_file function
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as fh:
        lines = fh.read()
        print(lines, end="")
