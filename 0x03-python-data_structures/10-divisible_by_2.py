#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    length = len(my_list)
    if length > 0:
        for i in range(length):
            if my_list[i] % 2 == 0:
                list_result.append(True)
            else:
                list_result.append(False)
    return list_result
