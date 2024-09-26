#!/usr/bin/python3
"""Module that defines a Square class, inheriting from the Rectangle class.

This module imports the Rectangle class from another module and provides
a Square class that validates its size and calculates its area.
"""

Rec = __import__('9-rectangle').Rectangle


class Square(Rec):
    """Represents a square, inheriting from the Rectangle class.

    This class validates the size of the square and calculates its area.

    Attributes:
        __size (int): The size of the square, which sets both width and height.
    """

    def __init__(self, size):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square, which sets both width and
            height.

        Raises:
            ValueError: If size is not a positive integer.
            TypeError: If size is not an integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the Square instance.

        Returns:
            str: A string in the format "[Square] size/size".
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square, calculated as size * size.
        """
        return self.__size * self.__size
