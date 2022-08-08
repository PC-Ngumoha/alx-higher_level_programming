#!/usr/bin/python3
"""Module containing the ``Base`` class definition.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string representation of a list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the actual object represented by the json string.
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            objs = "[]"
        else:
            obj_dicts = []
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                obj_dicts.append(obj_dict)
            objs = Base.to_json_string(obj_dicts)
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            f.write(objs)
