#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        length = len(my_list)
        if length == 0:
            return
        largest = my_list[0]
        for i in range(1, length):
            if my_list[i] > largest:
                largest = my_list[i]
        return largest
    else:
        return
