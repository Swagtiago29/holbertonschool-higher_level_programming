#!/usr/bin/python3
def read_file(filename=""):
    """
    Read and print the contents of a text file.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string,
                        which may lead to an error if no filename is provided.

    Example:
        read_file("example.txt")
    """
    with open(filename, 'r') as f:
        rid = f.read()
    print(rid)
