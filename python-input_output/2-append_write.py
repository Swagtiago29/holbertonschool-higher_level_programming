#!/usr/bin/python3

"""
This module provides a function to append text to a specified file.

Usage:
    Call the `append_write` function with the filename and text as arguments.

Example:
    append_write("example.txt", "This text will be appended.")
"""


def append_write(filename="", text=""):
    """
    Append the specified text to a file.

    Args:
        filename (str): The name of the file where the text will be appended. 
                         If the file does not exist, it will be created.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters appended to the file.

    Raises:
        IOError: If an error occurs while writing to the file.

    Example:
        append_write("example.txt", "This text will be appended.")
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
