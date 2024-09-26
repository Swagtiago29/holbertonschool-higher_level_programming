#!/usr/bin/python3
"""
MyList Module

This module defines the MyList class, which inherits from the built-in
list class.
It includes a method to print the elements of the list in sorted order.
"""


class MyList(list):
    """
    MyList Class

    Inherits from the built-in list class and provides a method to print
    the list in sorted (ascending) order.

    Methods
    -------
    print_sorted():
        Prints the elements of the list in ascending order.
    """

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.

        This method creates a sorted copy of the list and prints it
        The original list remains unchanged.
        """
        sorted_list = sorted(self)
        print(sorted_list)
