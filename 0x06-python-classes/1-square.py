#!/usr/bin/python3
"""
This is module-level documentation
In this module we define a Square
"""


class Square:
    """
    This is a'Square'
    Has a private attribute 'size'
    """

    __size = 0

    def __init__(self, size=0):
        """
        Instantiate 'size' attribute safely
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
