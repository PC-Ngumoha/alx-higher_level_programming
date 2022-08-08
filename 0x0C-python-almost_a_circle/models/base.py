#!/usr/bin/python3
"""Module containing the ``Base`` class definition.
"""
import json
import os.path


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
        """saves list of objects to files.
        """
        if list_objs is None:
            objs = "[]"
        else:
            obj_dicts = []
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                obj_dicts.append(obj_dict)
            objs = Base.to_json_string(obj_dicts)
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(objs)

    @classmethod
    def create(cls, **dictionary):
        """creates a new object from the values in dictionary.
        """
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Creates a new instance of the class from the contents of a file.
        """
        filename = "{}.json".format(cls.__name__)
        list_objs = []
        if not os.path.exists(filename):
            return []
        else:
            with open(filename, 'r', encoding='utf-8') as file:
                json_string = file.read()
            list_dictionaries = Base.from_json_string(json_string)
            for dictionary in list_dictionaries:
                obj = cls.create(**dictionary)
                list_objs.append(obj)
            return list_objs
