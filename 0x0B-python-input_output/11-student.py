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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the instance of the class.
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = dict()
            old_dict = self.__dict__
            for (key, value) in old_dict.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

    def reload_from_json(self, json):
        """Uses the ``json`` dictionary to set the attributes of the instance.
        """
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
