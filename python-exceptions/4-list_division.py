#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    niu_list=[]
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            niu_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            niu_list.append(0)
        except TypeError:
            print("wrong type")
            niu_list.append(0)
        except IndexError:
            print("ourt of range")
            niu_list.append(0)
    return niu_list
