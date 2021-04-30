#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    argc = len(argv) - 1
    if argc == 0:
        print("0")
    else:
        for i in range(1, argc + 1):
            result += int(argv[i])
        print(result)
