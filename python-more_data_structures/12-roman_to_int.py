#!/usr/bin/python3
def checks(romano):
    if 'I' == romano:
        return 1
    if 'X' == romano:
        return 10
    if 'C' == romano:
        return 100
    if 'M' == romano:
        return 1000
    if 'V' == romano:
        return 5
    if 'L' == romano:
        return 50
    if 'D' == romano:
        return 500


def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        x = 0
        for i in range(len(roman_string)):
            if len(roman_string) == 1:
                return checks(roman_string[i])
            elif len(roman_string) > i + 1:
                if checks(roman_string[i]) > checks(roman_string[i + 1]):
                    x += checks(roman_string[i])
                elif checks(roman_string[i]) == checks(roman_string[i + 1]):
                    x += checks(roman_string[i])
                else:
                    x -= checks(roman_string[i])
            elif len(roman_string) == i + 1:
                roman_string[i] <= roman_string[i - 1]
                x += checks(roman_string[i])
        return x
    else:
        return 0
