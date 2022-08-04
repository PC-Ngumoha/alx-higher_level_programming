#!/usr/bin/python3
"""Module containing the ``Base`` class definition.
"""


class Base:
    """``Base`` class definition.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes objects of class ``Base``.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
