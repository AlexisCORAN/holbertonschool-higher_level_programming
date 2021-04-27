#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

str = "Last digit of"

if number < 0:
    last_digit = number % -10
elif number >= 0:
    last_digit = number % 10

if last_digit < 6 and last_digit != 0:
    str01 = "and is less than 6 and not 0"
    print("{} {} is {} {}".format(str, number, last_digit, str01))
elif last_digit == 0:
    print("{} {} is {} and is 0".format(str, number, last_digit))
elif last_digit > 5:
    str01 = "and is greater than 5"
    print("{} {} is {} {}".format(str, number, last_digit, str01))
