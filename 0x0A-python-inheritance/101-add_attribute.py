#!/usr/bin/python3
"""Module containing the ``add_attribute`` function definition.
"""


def add_attribute(obj, name, value):
    """adds an attribute to an object.
    Args:
        obj (object): object we want to extend
        name (str): name of attribute to add
        value (any type): value of attribute to add
    """
    if type(obj) in (int, float, str, list, tuple, set, dict):
        raise TypeError("can't add new attribute")
    elif hasattr(obj, name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
