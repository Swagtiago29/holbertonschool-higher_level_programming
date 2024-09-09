#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list) +1 
    for i in range (1, x):
        print("{:d}".format(my_list[-i]))
