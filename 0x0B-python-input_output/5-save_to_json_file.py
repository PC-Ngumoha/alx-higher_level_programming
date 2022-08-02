#!/usr/bin/python3
"""Module containing the ``save_to_json_file`` function definition.
"""
import json


def save_to_json_file(my_obj, filename):
    """saves the JSON string representation of ``my_obj`` to a .json file.
    """
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(my_obj, fp)
