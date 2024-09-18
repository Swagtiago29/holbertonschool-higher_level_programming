#!/usr/bin/python3

"""
square.py

This module defines a Square class that represents a square shape.
"""

class Square:
    """A class to represent a square.

    Attributes:
    ----------
    __size : int or float
        The length of a side of the square, set during instantiation.
    """

    def __init__(self, size):
        """Initialize the Square with a given size.

        Parameters:
        ----------
        size : int or float
            The length of a side of the square.
        """
        self.__size = size
