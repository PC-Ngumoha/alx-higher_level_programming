#!/usr/bin/python3
'''Contains code that determines the peak point in a series of data points
'''


def find_peak(points):
    '''Gets the peak'''
    lim = len(points)
    if lim == 0:
        return
    if lim == 1:
        return points[0]
    elif lim == 2:
        return max(points)

    pos = lim // 2
    peak = points[pos]
    if peak > points[pos + 1] and peak > points[pos - 1]:
        return peak
    if peak < points[pos + 1]:
        return find_peak(points[pos + 1:])
    else:
        return find_peak(points[:pos])
