#!/usr/bin/python3
"""Module containing the ``load_from_json_file`` function definition.
"""
import json


def load_from_json_file(filename):
    """loads the JSON string data from a file.
    """
    with open(filename, 'r', encoding='utf-8') as fp:
        new_obj = json.load(fp)
        return new_obj
