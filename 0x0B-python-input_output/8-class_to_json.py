#!/usr/bin/python3
"""Module containing ``class_to_json`` function definition.
"""


def class_to_json(obj):
    """returns a serialization of ``obj``.
    """
    return obj.__dict__
