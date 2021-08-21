#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header.get("X-Request-Id"))
