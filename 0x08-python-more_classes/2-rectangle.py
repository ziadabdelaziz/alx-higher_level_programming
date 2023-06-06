#!/usr/bin/python3
"""
This module includes an empty rectangle
"""


class Rectangle:
    """
    rectangle
    """

    def __init__(self, width=0, height=0):
        """
        instanciate the rectangle with
        width and height
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """
        width getter
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        make sure the width is integer
        and not negative
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        make sure the height is integer
        and not negative
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        return area of rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        return perimeter of rectangle
        """

        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
