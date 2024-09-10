#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    liston = my_list
    for i in my_list:
        if i % 2 == 0:
            liston[i] = "True"
        else:
            liston[i] = "False"
    return liston
