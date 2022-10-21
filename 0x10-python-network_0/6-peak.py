#!/usr/bin/python3
'''Contains code that determines the peak point in a series of data points
'''


def find_peak(points):
    '''Gets the peak'''
    pos = 1
    peak = None
    while pos < len(points):
        if points[pos - 1] <= points[pos] and points[pos + 1] <= points[pos]:
            peak = points[pos]
            break
        else:
            pos += 1
    return peak
