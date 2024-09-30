#!/usr/bin/python3

"""
This module provides a function to save a Python object to a JSON file.

Usage:
    Call the `save_to_json_file` function with a Python object and a filename
    as arguments.

Example:
    save_to_json_file({"key": "value"}, "output.json")
"""


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a JSON file.

    Args:
        my_obj (object): The Python object to serialize and save.
        filename (str): The name of the file where the JSON object will be
        saved.

    Returns:
        None

    Raises:
        IOError: If an error occurs while writing to the file.

    Example:
        save_to_json_file({"key": "value"}, "output.json")
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
