#!/usr/bin/python3
def print_list_integer(my_list=[]):

    for num in my_list:
        if num >= 0:
            print("{:d}".format(num))
