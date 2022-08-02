#!/usr/bin/python3
"""Module containing the ``to_json_string`` function definition.
"""
import json


def to_json_string(my_obj):
    """Returns the json representation of ``my_obj``.
    """
    json_string = json.dumps(my_obj)
    return json_string
