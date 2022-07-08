#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is not None:
        weighted_numerator = 0
        weight_sum = 0
        for score, weight in my_list:
            weighted_numerator += (score * weight)
            weight_sum += weight
        average = (weighted_numerator / weight_sum)
        return average
