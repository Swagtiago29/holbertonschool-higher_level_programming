#!/usr/bin/python3
class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Args:
            size (int): The size of the square's side:
            cannot be negative.

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
