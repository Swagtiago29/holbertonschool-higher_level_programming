#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        if c is None:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(c))
    return c
