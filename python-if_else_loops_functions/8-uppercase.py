#!/usr/bin/python3
def uppercase(str):

    i = 0
    x = len(str)
    for str[i] in range (x, 1):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            ord(str[i]) - 32
            print(chr(str[i]), end= '')
        else:
            print(str[i], end= '')
    print()
