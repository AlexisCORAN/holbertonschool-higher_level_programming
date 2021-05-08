#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        tot = 0
        div= 0
        for x in my_list:
            tot += x[0] * x[1]
            div += x[1]
        return (tot / div)
    return 0
