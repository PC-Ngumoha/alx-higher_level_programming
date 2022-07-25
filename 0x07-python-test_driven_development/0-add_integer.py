#!/usr/bin/python3
"""Module contains the ``add_integer`` function.
"""


def add_integer(a, b=98):
    """Adds two integers and produces output.
    Args:
        a (int): first integer parameter.
        b (int): second integer (optional) parameter.
    Raises:
        TypeError: if any of the arguments is not an integer or float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
