#!/usr/bin/python3
def uppercase(str):

    i = 0
    x = len(str)
    for i in range (0, x, 1):
        o = ord(str[i]) 
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            o - 32
        print("{}".format(chr(o)), end= '')
    print()
