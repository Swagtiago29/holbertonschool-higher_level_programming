#!/usr/bin/python3

"""
Module: square
This module defines a class that represents a square and provides methods
to calculate its area.
"""


class Square:
    """Represents a square with a specified size.

    Attributes:
        __size (int): The size of the square's side
        must be a non-negative integer.
    """

    def __init__(self, size=0):
        """Initializes the Square instance.

        Args:
            size (int): The size of the square's side. Defaults to 0.

        Raises:
            ValueError: If size is a negative integer.
            TypeError: If size is not an integer.
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square, calculated as size * size.
        """
        aria = self.__size
        return aria * aria
