#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in reversed(my_list):
        if isinstance(num, int):
            print("{:d}".format(num))
