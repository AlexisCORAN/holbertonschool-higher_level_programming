#!/usr/bin/python3
"""
This module defines the save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, mode="w") as fh:
        json.dump(my_obj, fh)
