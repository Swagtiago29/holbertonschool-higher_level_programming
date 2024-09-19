#!/usr/bin/python3

"""
Module: square
This module defines a class that represents a square and provides methods
to calculate its area and print a visual representation of the square.
"""


class Square:
    """Represents a square with a specified size.

    Attributes:
        __size (int): The size of the square's side.
        Must be a non-negative integer.
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

    @property
    def size(self):
        """int: The size of the square's side.

        Getter for the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square's side.

        Raises:
            ValueError: If value is a negative integer.
            TypeError: If value is not an integer.
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square, calculated as size * size.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints a visual representation of the square using the '#' character

        If the size of the square is greater than 0, it prints a square
        of '#' characters. The square will have dimensions of size x size.

        If the size is 0, it prints an empty line.

        Example:
            If the size is 3, the output will be:
            ###
            ###
            ###
        """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    if j != self.__size - 1:
                        print("#", end='')
                    else:
                        print("#")
        else:
            print()
