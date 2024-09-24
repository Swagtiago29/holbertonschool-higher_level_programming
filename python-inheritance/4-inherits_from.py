#!/usr/bin/python3
"""
Module: Inheritance Checking

This module provides a function to check if an object is an instance
of a class that inherits (directly or indirectly) from a specified class,
excluding direct instances of that class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherits
    (directly or indirectly) from the specified class.

    Parameters
    ----------
    obj : any
        The object to be checked.
    a_class : type
        The class to be compared against.

    Returns
    -------
    bool
        True if the object is an instance of a class that inherited
        from the specified class, otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
