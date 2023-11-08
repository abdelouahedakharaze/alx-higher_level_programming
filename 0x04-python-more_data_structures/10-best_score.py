#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max_score = max(a_dictionary.values())
    max_key = None
    for key, value in a_dictionary.items():
        if value == max_score:
            max_key = key
            break
    return max_key
