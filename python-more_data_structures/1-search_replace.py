#!/usr/bin/python3
def search_replace(my_list, search, replace):
    niu_list = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] == search:
            niu_list[i] = replace
    return niu_list
