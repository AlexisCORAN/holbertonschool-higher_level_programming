#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    else:
        for num in my_list:
            if num == idx:
                break
        return (num)
