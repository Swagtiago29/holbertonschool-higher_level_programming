#!/usr/bin/python3
def no_c(my_string):
    x = len(my_string)
    for i in range(x):
        if my_string[i] == 'C' or my_string[i] == 'c':
            if i == 0:
                str = my_string[i + 1:]
            else:
                str = my_string[: i] + my_string[i + 1:]
    return str
