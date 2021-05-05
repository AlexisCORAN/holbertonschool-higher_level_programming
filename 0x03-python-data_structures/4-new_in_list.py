#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0:
        return (new_list)
    else:
        for count, num in enumerate(my_list):
            if count == idx:
                my_list[count] = element
                return (new_list)
        else:
            return (new_list)
