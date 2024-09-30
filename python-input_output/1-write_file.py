#!/usr/bin/python3

"""
This module provides a function to write text to a specified file.

Usage:
    Call the `write_file` function with the filename and text as arguments.

Example:
    write_file("example.txt", "Hello, World!")
"""


def write_file(filename="", text=""):
    """
    Write the specified text to a file.

    Args:
        filename (str): The name of the file where the text will be written.
                         If the file does not exist, it will be created.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.

    Raises:
        IOError: If an error occurs while writing to the file.

    Example:
        write_file("example.txt", "Hello, World!")
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
