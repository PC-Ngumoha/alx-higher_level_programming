#!/usr/bin/python3
"""Module containing the ``is_kind_of_class`` function definition.
"""


def is_kind_of_class(obj, a_class):
    """Determines if ``obj`` is an instance of ``a_class`` or any of
    it's subclasses.
    Args:
        obj (object): object to be evaluated.
        a_class: class to check ``obj`` against.
    Returns:
        True: if ``obj`` is an instance of ``a_class`` or it's subclass
        False: Otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
