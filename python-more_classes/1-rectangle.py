#!/usr/bin/python3
"""Module for rectangle representation.

This module defines the Rectangle class, which models a rectangle
with a specified width and height. The class includes input validation
for the dimensions to ensure they are non-negative integers.
"""


class Rectangle:
    """A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        Must be a non-negative integer.
        height (int): The height of the rectangle.
        Must be a non-negative integer.

    Methods:
        __init__(width, height): Initializes a new Rectangle instance.
        height: Getter and setter for the height attribute.
        width: Getter and setter for the width attribute.
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """Getter for height.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

    @property
    def width(self):
        """Getter for width.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')
