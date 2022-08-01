#!/usr/bin/python3

"""Module contains definition of ``Rectangle`` class.
A subclass of the ``BaseGeometry`` class.
"""


base_geometry = __import__("7-base_geometry")


class Rectangle(base_geometry.BaseGeometry):
    """``Rectangle`` class definition.
    """
    def __init__(self, width, height):
        """Initializes the attributes of class ``Rectangle``
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns string representation of instance of class ``Rectangle``
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Computes the area of instance of class ``Rectangle``
        """
        return self.__width * self.__height
