#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if b != 0: 
            c = a / b
            print("Inside result: {:.1f}".format(c))
            return c
    except (ValueError, TypeError):
        print("inside result: {}".format(None))
        return None