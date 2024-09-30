#!/usr/bin/python3

"""
This module provides a function to load a Python object from a JSON file.

Usage:
    Call the `load_from_json_file` function with a filename as an argument.

Example:
    my_obj = load_from_json_file("input.json")
"""

def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.

    Args:
        filename (str): The name of the file from which to read the JSON object.

    Returns:
        object: The Python object represented by the JSON data in the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If an error occurs while reading the file.

    Example:
        my_obj = load_from_json_file("input.json")
    """
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)