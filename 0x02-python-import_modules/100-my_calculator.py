#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])
        operator = ["+", "-", "*", "/"]
        function = [add, sub, mul, div]
        for i, op in enumerate(operator):
            if argv[2] == op:
                print("{} {} {} = {}".format(a, op, b, function[i](a, b)))
                break
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
