#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
"""
from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
