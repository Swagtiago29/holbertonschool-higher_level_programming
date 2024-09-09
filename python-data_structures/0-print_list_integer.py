#!/usr/bin/python3
def print_list_integer(my_list=[]):
    o = len(my_list)
    for i in range(0, o):
        print("{:d}".format(my_list[i]))
