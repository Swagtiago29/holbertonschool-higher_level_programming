#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dictionary = a_dictionary.sort()
    for i in b_dictionary:
        x = a_dictionary.get(i)
        print("{}: {}".format(i, x))
