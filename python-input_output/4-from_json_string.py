#!/usr/bin/python3

"""
This module provides a function to convert a JSON string to a Python object.

Usage:
    Call the `from_json_string` function with a JSON string as an argument.

Example:
    python_obj = from_json_string('{"key": "value"}')
"""


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Args:
        my_str (str): A JSON string representation of a Python object.

    Returns:
        object: The Python object represented by the JSON string.

    Example:
        python_obj = from_json_string('{"key": "value"}')
    """
    import json
    return json.loads(my_str)
