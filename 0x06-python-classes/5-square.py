#!/usr/bin/python3
"""Module that contains the ``Square`` class definition.
"""


class Square:
    """Class ``Square`` definition.
    """
    def __init__(self, size=0):
        """Initializes the attributes of the ``Square`` class.
        Args:
            size (int): size of the ``Square``.
        """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    @property
    def size(self):
        """``size`` property.
        @size.setter
        Args:
            value (int): value to set the size of the ``Square``
        Raises:
            TypeError: if ``value`` is not an int.
            ValueError: if ``value`` is less than zero.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Calculates the area of the square
        Returns:
            Area of Square if successful, 0 if nothing is supplied
        """
        return self.__size ** 2

    def my_print(self):
        """Prints out the Square to the screen using the `#` symbol
        Returns:
            None
        """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
