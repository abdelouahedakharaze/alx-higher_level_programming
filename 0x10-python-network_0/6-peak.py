#!/usr/bin/python3
"""find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    # just to make it shorter for the linter 80 char.
    li = list_of_integers
    lenght = len(li)
    if lenght == 0:
        return
    m = lenght // 2
    if (m == lenght - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != lenght - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
