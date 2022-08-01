#!/usr/bin/python3
"""Module contains the definition of class ``Square``.
subclass of class ``Rectangle``.
"""
rectangle = __import__("9-rectangle")


class Square(rectangle.Rectangle):
    """``Square`` class definition.
    """
    def __init__(self, size):
        """Initialize the ``size`` attribute of the ``Square``
        class.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns the string representation of an instance of class
        ``Square``.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Computes the area of instance of ``Square``
        """
        return self.__size ** 2
