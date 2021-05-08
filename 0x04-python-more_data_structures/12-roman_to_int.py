#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    if roman_string is None or roman_string != str:
        return none
    num = 0
    for i in range(len(roman_string)):
        if i > 0 and roman[roman_string[i]] > roman[roman_string[i - 1]]:
            num += roman[roman_string[i]] - 2 * roman[roman_string[i - 1]]
        else:
            num += roman[roman_string[i]]
    return (num)
