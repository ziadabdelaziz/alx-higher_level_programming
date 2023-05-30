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

    def __init__(self, size=0):
        """
        Instantiate 'size' attribute safely
        """

        self.size = size

    def area(self):
        """
        Returns the area of the square
        """

        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter function for 'size'
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter function for 'size'
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
