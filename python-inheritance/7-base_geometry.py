#!/usr/bin/python3
"""
Module: Geometry

This module defines the BaseGeometry class, which serves as a base
class for other geometric shapes. It includes a method to calculate
the area, which must be implemented by subclasses.
"""


class BaseGeometry:
    """
    BaseGeometry Class

    This is a base class intended for future geometric shape
    implementations. It provides a common interface for geometric
    shapes and defines a method for calculating the area.

    Attributes
    ----------
    None

    Methods
    -------
    area():
        Raises an Exception indicating that the area method is not
        implemented. This method should be overridden in subclasses.

    integer_validator(name, value):
        Validates that the value is a positive integer.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises
        ------
        Exception
            Always raises an Exception indicating that the method
            is not implemented. Subclasses must override this method
            to provide a specific implementation for calculating the area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is a positive integer.

        Parameters
        ----------
        name : str
            The name of the parameter being validated.
        value : any
            The value to be validated.

        Raises
        ------
        TypeError
            If value is not an integer.
        ValueError
            If value is an integer but less than or equal to 0.
        """
        if type(value) is int:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
        else:
            raise TypeError(f"{name} must be an integer")
