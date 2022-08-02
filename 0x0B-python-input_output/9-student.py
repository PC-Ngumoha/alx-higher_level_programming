#!/usr/bin/python3
"""Module containing the ``Student`` class definition.
"""


class Student:
    """``Student`` class definition.
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the instance of the class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of the instance of the class.
        """
        return self.__dict__
