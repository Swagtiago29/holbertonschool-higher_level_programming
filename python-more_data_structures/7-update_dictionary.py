#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dic = a_dictionary
    if key in a_dictionary:
        new_dic[key] = value
    if key not in a_dictionary:
        new_dic[key] = value
    return new_dic
