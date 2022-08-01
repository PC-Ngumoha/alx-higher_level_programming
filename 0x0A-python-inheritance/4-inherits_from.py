#!/usr/bin/python3
"""Module contains the function ``inherits_from`` definition.
"""


def inherits_from(obj, a_class):
    """Determines if ``obj`` is an instance of a class which is a
    subclass of ``a_class``.
    Args:
        obj (object): object to be evaluated.
        a_class (class): class to be evaluated against.
    Returns:
        True: if ``obj`` is instance of subclass of ``a_class``
        False: if otherwise.
    """
    obj_type = type(obj)
    if issubclass(obj_type, a_class) and obj_type != a_class:
        return True
    else:
        return False
