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

    def update(self, *args, **kwargs):
        """Updates each attribute of the class
        """
        if args is not None and len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                id, size = args
                self.id = id
                self.size = size
            elif len(args) == 3:
                id, size, x = args
                self.id = id
                self.size = size
                self.x = x
            elif len(args) == 4:
                id, size, x, y = args
                self.id = id
                self.size = size
                self.x = x
                self.y = y
        else:
            if kwargs is not None:
                for key in kwargs.keys():
                    if key == 'id':
                        self.id = kwargs[key]
                    elif key == 'size':
                        self.size = kwargs[key]
                    elif key == 'x':
                        self.x = kwargs[key]
                    elif key == 'y':
                        self.y = kwargs[key]

    def to_dictionary(self):
        """returns the dictionary representation of the ``Square``
        instance
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
