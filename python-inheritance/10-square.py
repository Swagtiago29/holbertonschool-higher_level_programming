#!/usr/bin/python3
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
            size (int): The size of the square, which sets both width and height.

        Raises:
            ValueError: If size is not a positive integer.
            TypeError: If size is not an integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
