#!/usr/bin/python3
"""Module containing the ``Square`` class with a private instance attribute
``size``.
"""


class Square:
    """Class ``Square`` definition.
    """
    def __init__(self, size):
        """Initialize the attributes of the ``Square`` class.

        Args:
            size (int): first parameter. Defines the size of the Square

        """
        self.__size = size
