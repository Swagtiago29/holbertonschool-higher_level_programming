#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        c = None
    finally:
        if c is None:
            print("Inside Result: None")
        else:
            print("Inside Result: {:.1f}".format(c))
    return c
