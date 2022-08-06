#!/usr/bin/python3
"""Module containing ``Square`` class definition.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """``Square`` class definition
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize instance of ``Square`` class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """public ``size`` property"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
