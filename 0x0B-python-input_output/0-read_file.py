#!/usr/bin/python3
"""Module containing ``read_file`` function definition.
"""


def read_file(filename=""):
    """reads the contents of a file and prints it out to the screen.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
