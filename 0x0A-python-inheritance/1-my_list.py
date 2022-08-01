#!/usr/bin/python3
"""Module containing the ``MyList`` class definition."""


class MyList(list):
    """``MyList`` class definition."""
    def print_sorted(self):
        """prints out the content of the list in a sorted order."""
        print(sorted(self))
