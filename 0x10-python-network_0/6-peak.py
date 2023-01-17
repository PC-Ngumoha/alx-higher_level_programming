#!/usr/bin/python3
'''Contains code that determines the peak point in a series of data points
'''


def find_peak(points):
    '''Gets the peak'''
    lim = len(points)
    if lim == 0:
        return
    pos = lim // 2
    if (pos == lim - 1 or points[pos] >= points[pos + 1]) and \
            (pos == 0 or points[pos] >= points[pos - 1]):
        return points[pos]
    if pos != lim - 1 and points[pos + 1] > points[pos]:
        return find_peak(points[pos + 1:])
    return find_peak(points[:pos])
