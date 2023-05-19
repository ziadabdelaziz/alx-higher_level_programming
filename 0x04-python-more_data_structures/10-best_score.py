#!/usr/bin/python3
def best_score(a_dictionary):
    max = float('-inf')
    key = None

    if not a_dictionary:
        return None

    for key in a_dictionary:
        if a_dictionary[key] > max:
            max = a_dictionary[key]

    return key
