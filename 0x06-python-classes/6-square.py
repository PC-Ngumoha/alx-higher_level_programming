#!/usr/bin/python3
"""Module that contains the ``Square`` class definition.
"""


class Square:
    """Class ``Square`` definition.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the attributes of the ``Square`` class.
        Args:
            size (int): size of the ``Square``
            position (tuple): coordinates of the ``Square``
        """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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

    @property
    def position(self):
        """``position`` property
        @position.setter
        Args:
            position: coordinates of the square
        Raises:
            TypeError: if ``position`` is not a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, position):
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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
        else:
            # Prints the vertical offset of the square
            for y in range(self.__position[1]):
                print()
        for i in range(self.__size):
            # Prints the horizontal offset of the square
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
