#!/usr/bin/python3
"""Module containing definition of a version of the ``Rectangle``
class.
"""


class Rectangle:
    """Definition of the ``Rectangle`` class.
    """
    def __init__(self, width=0, height=0):
        """Called when the object is created.
        Args:
            width (int): first parameter. Defines width of rectangle.
            height (int): second parameter. Defines height of rectangle.
        Raises:
            TypeError: If any of the parameters is not an integer.
            ValueError: If the value of any of the parameters is < 0.
        """
        if type(width) == int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if type(height) == int:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """``width`` property.
        Args:
            value (int): sets the value of the width variable.
        Raises:
            TypeError: If ``value`` is not an integer.
            ValueError: If ``value`` < 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """``height`` property.
        Args:
            value (int): sets the value of the height variable.
        Raises:
            TypeError: If ``value`` is not an integer.
            ValueError: If ``value`` < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
