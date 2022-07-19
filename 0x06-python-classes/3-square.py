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

    def area(self):
        """Calculates the area of the square

        Returns:
            Area of Square if successful, 0 if nothing is supplied
        """
        return self.__size ** 2
