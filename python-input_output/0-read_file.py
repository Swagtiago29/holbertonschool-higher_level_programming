#!/usr/bin/python3

"""
This module provides a function to read and print the contents of a specified
text file.

Usage:
    Call the `read_file` function with the filename as an argument.

Example:
    read_file("example.txt")
"""


def read_file(filename=""):
    """
    Read and print the contents of a text file.

    Args:
        filename (str): The name of the file to read. Defaults to an
                        empty string which may lead to an error if 
                        no filename is provided.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: For any other errors encountered while opening or
        reading the file.

    Example:
        read_file("example.txt")
    """
    with open(filename, encoding='utf-8') as f:
        rid = f.read()
    print(rid, end='')
