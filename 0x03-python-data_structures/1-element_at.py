#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    else:
        for count, num in enumerate(my_list):
            if count == idx:
                return (num)
        else:
            return (None)
