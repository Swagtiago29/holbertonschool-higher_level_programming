#!/usr/bin/python3

"""
lookup.py

This module provides a function to retrieve the list of attributes and methods 
of a given object.

Functions:
    lookup(obj): Returns a list of attributes and methods of the object.

Usage:
    Import the module and call the lookup function with an object as the argument.

Example:
    import lookup
    class MyClass:
        def method(self):
            pass

    instance = MyClass()
    print(lookup(instance))  # Output will be a list of attributes and methods of instance.
"""

def lookup(obj):
    """
    Return a list of attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods are to be retrieved.

    Returns:
        A list of strings, representing the names of the attributes and methods
        of the given object.
    """
    return dir(obj)
