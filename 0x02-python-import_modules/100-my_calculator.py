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
        if operator == "+":
            result = add(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == "-":
            result = sub(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == "*":
            result = mul(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == "/":
            if b == 0:
                print("Invalid second argument")
                exit(0)
            else:
                result = div(a, b)
                print("{} {} {} = {}".format(a, operator, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
