#!/usr/bin/python3
"""
This module defines the read_file function
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as fh:
        print(fh.read(), end="")
