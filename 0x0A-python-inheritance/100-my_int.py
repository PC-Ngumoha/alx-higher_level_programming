#!/usr/bin/python3
"""Module containing the ``MyInt`` class definition.
"""


class MyInt(int):
    """class ``MyInt`` definition.
    """
    def __new__(cls, value):
        """Creates an instance of the ``MyInt`` class.
        """
        return super().__new__(cls, value)

    def __eq__(self, other):
        """Overloading the == operator.
        """
        res = super(MyInt, self).__eq__(other)
        return not res

    def __ne__(self, other):
        """Overloading the != operator.
        """
        res = super(MyInt, self).__ne__(other)
        return not res
