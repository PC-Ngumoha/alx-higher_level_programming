#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    num_print = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            i += 1
        else:
            num_print += 1
            i += 1
    print()
    return num_print
