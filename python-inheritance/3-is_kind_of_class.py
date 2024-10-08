#!/usr/bin/python3
"""
Module: Type Checking

This module provides a function to check if an object is an instance
of a specified class or a subclass thereof.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class or a subclass.

    Parameters
    ----------
    obj : any
        The object to be checked.
    a_class : type
        The class to be compared against.

    Returns
    -------
    bool
        True if the object is an instance of the specified class or
        any subclass, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
