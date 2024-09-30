#!/usr/bin/python3

"""
This module provides a function to convert a Python object to a JSON string.

Usage:
    Call the `to_json_string` function with a Python object as an argument.

Example:
    json_string = to_json_string({"key": "value"})
"""


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string.

    Args:
        my_obj (object): The Python object to convert to JSON format.

    Returns:
        str: A JSON string representation of the input object.

    Example:
        json_string = to_json_string({"key": "value"})
    """
    import json
    return json.dumps(my_obj)
