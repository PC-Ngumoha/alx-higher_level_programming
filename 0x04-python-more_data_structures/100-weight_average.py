#!/usr/bin/python3

def weight_average(my_list=[]):
    weighted_numerator = 0
    weight_sum = 0
    for value, weight in my_list:
        weighted_numerator += (value * weight)
        weight_sum += weight
    average = (weighted_numerator / weight_sum)
    return average
