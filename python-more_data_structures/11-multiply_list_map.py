#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mults = map(lambda number: number * 2, my_list)
    return list(mults)