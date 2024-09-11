#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for i in a_dictionary:
        x = a_dictionary.get(i)
        b_dictionary[i] = x * 2
    return b_dictionary
