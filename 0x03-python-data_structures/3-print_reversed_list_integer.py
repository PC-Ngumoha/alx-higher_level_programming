#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        last_idx = len(my_list) - 1
        for i in range(last_idx, -1, -1):
            print("{:d}".format(my_list[i]))
