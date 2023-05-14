#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if 0 > idx:
        return None

    if  idx >= len(my_list):
        return None

    my_list[idx] = element
    return my_list
