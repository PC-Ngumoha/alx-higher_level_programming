#!/usr/bin/python3
"""Module containing the ``append_write`` function definition.
"""


def append_write(filename="", text=""):
    """appends the ``text`` to file ``filename``.
    """
    num_char = 0
    with open(filename, 'a', encoding="utf-8") as f:
        num_char = f.write(text)
    return num_char
