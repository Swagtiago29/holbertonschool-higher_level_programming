#!/usr/bin/python3
def best_score(a_dictionary):
    x = 0
    if a_dictionary:
        for i in a_dictionary:
            if a_dictionary.get(i) > x:
                x = a_dictionary.get(i)
                f = i
        return f
