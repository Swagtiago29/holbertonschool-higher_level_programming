#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Parameters
    ----------
    obj : any
        The object to be checked.
    a_class : type
        The class to be compared against.

    Returns
    -------
    bool
        True if the object is an instance of the specified class, 
        otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
