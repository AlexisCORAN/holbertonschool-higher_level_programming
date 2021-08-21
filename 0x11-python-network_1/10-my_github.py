#!/usr/bin/python3
"""
Takes my Github credentials (username and password)
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(argv[1], argv[2])).json()
    print(req.get('id'))
