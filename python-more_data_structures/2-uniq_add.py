#!/usr/bin/python3
def uniq_add(my_list=[]):
    niu_list = []
    for i in (my_list):
        if i not in niu_list:
            niu_list.append(i)
    return sum(niu_list)
