#!/usr/bin/python3
def best_score(a_dictionary):
    mx = max(a_dictionary.values())
    for i, j in a_dictionary.items():
        if j == mx:
            return i
    return None
