#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    else:
        for count, num in enumerate(my_list):
            if count == idx:
                my_list[count] = element
                return (my_list)
        else:
            return (my_list)
