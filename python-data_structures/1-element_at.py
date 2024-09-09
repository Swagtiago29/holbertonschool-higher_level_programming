#!/usr/bin/python3
def element_at(my_list, idx):
    le = len(my_list) - 1
    if idx > le:
        print("None1")
    elif idx < 0:
        print("None2")
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
