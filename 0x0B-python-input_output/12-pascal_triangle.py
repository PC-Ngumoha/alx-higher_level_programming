#!/usr/bin/python3
"""Module containing the ``pascal_triangle`` function definition.
"""


def pascal_triangle(n):
    """Tabulates the pascal triangle for a specified number.
    """
    triangle = []
    prev = None
    if n <= 0:
        return []
    else:
        for i in range(n):
            row = []
            j = 0
            while j <= i:
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(prev[j - 1] + prev[j])
                j += 1
            prev = row.copy()
            triangle.append(row)
    return triangle
