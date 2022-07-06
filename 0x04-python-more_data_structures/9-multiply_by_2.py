#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    list_dict = a_dictionary.items()
    new_dict = dict(map(lambda x: (x[0], x[1] * 2), list_dict))
    return new_dict
