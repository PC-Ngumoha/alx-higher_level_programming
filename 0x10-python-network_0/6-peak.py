#!/usr/bin/python3
'''Contains code that determines the peak point in a series of data points
'''


def find_peak(points):
    '''Gets the peak'''
    l = len(points)
    if l == 0:
        return
    pos = l // 2
    if (pos == l - 1 or points[pos] >= points[pos + 1]) and \
            (pos == 0 or points[pos] >= points[pos - 1]):
        return points[pos]
    if pos != l-1 and points[pos + 1] > points[pos]:
        return find_peak(points[pos + 1:])
    return find_peak(points[:pos])
    
