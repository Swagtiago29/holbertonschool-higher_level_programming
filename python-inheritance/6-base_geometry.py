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
