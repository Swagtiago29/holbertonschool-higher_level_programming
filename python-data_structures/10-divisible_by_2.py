#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    liston = []
    for i in my_list:
        if i % 2 == 0:
            liston.append(True)
        else:
            liston.append(False)
    return liston
