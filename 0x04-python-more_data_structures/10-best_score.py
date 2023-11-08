#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    mx = max(a_dictionary.values())
    for i, j in a_dictionary.items():
        if j == mx:
            return None
    return None
