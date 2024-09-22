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
        area(): Calculates and returns the area of the rectangle.
        perimeter(): Calculates and returns the perimeter of the rectangle.
        __str__(): Returns a string representation of the rectangle using '#'.
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

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """Returns a string representation of the rectangle using '#'.

        If the rectangle has zero width or height, an empty string is returned

        Returns:
            str: A visual representation of the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return ""
        return "\n".join('#' * self.width for _ in range(self.height))

    def __repr__(self):
        """Returns a string representation of the rectangle for developers.

        Returns:
            str: A string that represents the rectangle object.
        """
        return f"Rectangle(width={self.width}, height={self.height})"
