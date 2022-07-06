#!/usr/bin/python3

def uniq_add(my_list=[]):
    num_set = set(my_list)
    res = 0
    for i in num_set:
        res += i
    return res
