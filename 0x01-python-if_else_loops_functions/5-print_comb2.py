#!/usr/bin/python3

i = 0
while i <= 99:
    if i == 99:
        print("{:02d}".format(i))
        break
    print("{:02d}".format(i), end=", ")
    i += 1
