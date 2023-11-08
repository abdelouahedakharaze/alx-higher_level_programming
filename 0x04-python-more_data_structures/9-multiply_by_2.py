#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    rslt = dict()
    for i, j in a_dictionary.items():
        rslt[i] = j * 2
    return rslt
