#!/usr/bin/python3
class Square:
    """Represents a square with a specified size and position.

    Attributes:
        __size (int): The size of the square's side. Must be a non-negative integer.
        __position (tuple): A tuple representing the position of the square,
                           should contain two non-negative integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance with a given size and position.

        Args:
            size (int): The size of the square's side. Defaults to 0.
            position (tuple): A tuple of two positive integers representing the
                              position of the square. Defaults to (0, 0).

        Raises:
            ValueError: If size is a negative integer.
            TypeError: If size is not an integer or if position is not a tuple 
                        of two positive integers.
        
        This method validates the provided size and position. It ensures that 
        the size is a non-negative integer and that position is a tuple of 
        two non-negative integers. If the validations are successful, the size 
        and position are assigned to the instance variables.
        """
        if isinstance(position, tuple):
            for i in position:
                if isinstance(i, int) and i >= 0:
                    self.__position = position
                else:
                    raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """tuple: The current position of the square as a tuple of two non-negative integers.

        Getter for the position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): A tuple of two non-negative integers representing the
                           new position of the square.

        Raises:
            TypeError: If value is not a tuple of two non-negative integers.
        """
        if isinstance(value, tuple):
            for i in value:
                if isinstance(i, int) and i >= 0:
                    self.__position = value
                else:
                    raise TypeError("position must be a tuple of 2 positive integers")

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
        """Prints a visual representation of the square using the '#' character.

        If the size of the square is greater than 0, it prints a square
        of '#' characters. The square will have dimensions of size x size.

        If the size is 0, it prints an empty line. The square is positioned 
        according to the __position attribute, which determines how many 
        spaces to indent and how many new lines to print before the square.
        """
        if self.__size != 0:
            print('\n' * self.__position[1], end='')  # Moves down by the y-coordinate
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')  # Moves right by the x-coordinate
                for j in range(self.__size):
                    if j != self.__size - 1:
                        print("#", end='')
                    else:
                        print("#")
        else:
            print()
