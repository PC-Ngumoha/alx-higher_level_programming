#!/usr/bin/python3
"""Module contains the ``BaseGeometry`` class definition.
"""


class BaseGeometry:
    """``BaseGeometry`` class definition.
    """
    def area(self):
        """No implementation, so it raises an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value of a parameter.
        Args:
            name (str): name of the parameter.
            value (int): integer value of the parameter.
        Raises:
            TypeError: if ``value`` is not an integer.
            ValueError: if the value of ``value`` is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
