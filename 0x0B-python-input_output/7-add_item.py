#!/usr/bin/python3
"""
This module writes a script
"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    lst = load_from_json_file("add_item.json")
except FileNotFoundError:
    lst = []
lst.extend(argv[1:])
save_to_json_file(lst, "add_item.json")
