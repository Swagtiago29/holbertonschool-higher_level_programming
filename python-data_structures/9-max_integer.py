#!/usr/bin/python3
def max_integer(my_list=[]):
    
    if len(my_list) != 0:
        for i in range(1, len(my_list)):
            x = my_list[i - 1]
            if my_list[i] > x:
                x = my_list[i]
            else:
                pass
    else:
        return None
    return(x)
