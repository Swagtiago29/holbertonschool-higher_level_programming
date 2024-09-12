#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x:
        try:
            for i in range(x):
                if i == x - 1:
                    print("{:d}".format(my_list[i]))
                    return x
                else:
                    print("{:d}".format(my_list[i]), end='')
        except IndexError:
            print()
            return i
