#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        x = tuple_a[0] + tuple_b[0]
        y = tuple_b[1]
    elif len(tuple_b) < 2:
        x = tuple_a[0] + tuple_b[0]
        y = tuple_a[1]
    else:
        x = tuple_a[0] + tuple_b[0]
        y = tuple_a[1] + tuple_b[1]
    tuple_c=(x, y)
    return tuple_c