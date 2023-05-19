#!/usr/bin/python3
def best_score(a_dictionary):
    max = -99999999999999

    if len(a_dictionary) == 0:
        return None

    for key in a_dictionary:
        if a_dictionary[key] > max:
            max = a_dictionary[key]

    return max
