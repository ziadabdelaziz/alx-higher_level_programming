#!/usr/bin/python3
"""
This module inclues MyList class
inherits list
and have method that prints the list sorted
"""


class MyList(list):
    """
    inherits list
    but have print_sorted method
    """

    def print_sorted(self):
        """
        print list sorted
        """
        lst = self
        lst = sorted(lst)
        print(lst)
