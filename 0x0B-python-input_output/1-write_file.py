#!/usr/bin/python3
"""Module containing the ``write_file`` function definition.
"""


def write_file(filename="", text=""):
    """writes a piece of text to a file.
    """
    num_char = 0
    with open(filename, 'w', encoding="utf-8") as f:
        num_char = f.write(text)
    return num_char
