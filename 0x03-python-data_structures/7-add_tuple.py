#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return None
    elif len(tuple_a) == 0:
        return tuple_b
    elif len(tuple_b) == 0:
        return tuple_a
    else:
        if len(tuple_a) < 2 or len(tuple_b) < 2:
            if len(tuple_a) < 2:
                elem1 = tuple_a[0] + tuple_b[0]
                elem2 = tuple_b[1]
            elif len(tuple_b) < 2:
                elem1 = tuple_a[0] + tuple_b[0]
                elem2 = tuple_a[1]
        else:
            elem1 = tuple_a[0] + tuple_b[0]
            elem2 = tuple_a[1] + tuple_b[1]
        new_tuple = elem1, elem2
        return new_tuple
