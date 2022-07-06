#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = dict(sorted(a_dictionary.items(), key=lambda x: x[0]))
    for key in sorted_dictionary.keys():
        print("{:s}: {}".format(key, sorted_dictionary[key]))
