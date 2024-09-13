#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    o = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
            o += 1
    except IndexError:
        pass
    print()
    return o
