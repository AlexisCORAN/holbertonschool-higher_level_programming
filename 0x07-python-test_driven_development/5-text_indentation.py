#!/usr/bin/python3
"""
This is "5-test_indentation" module.
"""


def text_indentation(text):
    """ Function that prints indented text.

    Args:
        text (str): text to print
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for c in text:
        if flag == 0:
            if c == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if c == '?' or c == '.' or c == ':':
                print(c)
                print()
                flag = 0
            else:
                print(c, end="")
