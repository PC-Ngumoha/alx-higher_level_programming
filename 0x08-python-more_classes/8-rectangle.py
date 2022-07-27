#!/usr/bin/python3
"""Module containing definition of a version of the ``Rectangle``
class.
"""


class Rectangle:
    """Definition of the ``Rectangle`` class.
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1  # increase count of objects.

    def __str__(self):
        """Unofficial string representation of the Rectangle.
        """
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(self.print_symbol)
            if i < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """Official string representation of the Rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Called when an object of the class is deleted.
        """
        Rectangle.number_of_instances -= 1  # decrease count of objects.
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle with the biggest area.
        Args:
            rect_1 (Rectangle): first instance of class ``Rectangle``
            rect_2 (Rectangle): second instance of class ``Rectangle``
        Raises:
            TypeError: If any parameter is not an instance of ``Rectangle``
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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

    def area(self):
        """Calculates and returns the area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
