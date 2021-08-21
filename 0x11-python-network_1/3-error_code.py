#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError


if __name__ == "__main__":
    req = Request(argv[1])

    try:
        with urlopen(req) as responsive:
            print(responsive.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
