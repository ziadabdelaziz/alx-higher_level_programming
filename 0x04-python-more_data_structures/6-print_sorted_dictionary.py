#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary)
    for key in sorted_dictionary:
        print(f"{key}: {a_dictionary[key]}")
