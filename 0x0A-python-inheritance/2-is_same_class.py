#!/usr/bin/python3
"""Module that contains the ``is_same_class`` function.
"""


def is_same_class(obj, a_class):
    """Determines if ``obj`` is an instance of ``a_class``.
    Args:
        obj (any type): Object to be evaluated
        a_class (str): name of class to be checked against
    Returns:
        True: If ``obj`` is instance of ``a_class``
        False: If ``obj`` is not instance of ``a_class``
    """
    if type(obj) == a_class:
        return True
    else:
        return False
