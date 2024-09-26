#!/usr/bin/python3
"""Module that defines a Rectangle class, inheriting from BaseGeometry.

This module imports the BaseGeometry class from another module and
provides a Rectangle class that validates its dimensions.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle and validates its dimensions.

    Inherits from BaseGeometry and ensures that the width and height
    are positive integers.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If width or height is not a positive integer.
            TypeError: If width or height is not an integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
