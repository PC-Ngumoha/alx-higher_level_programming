#!/usr/bin/python3
"""Module containing the ``from_json_string`` function definition.
"""
import json


def from_json_string(my_str):
    """Returns an object formed from the deserialization of a JSON string.
    """
    new_obj = json.loads(my_str)
    return new_obj
