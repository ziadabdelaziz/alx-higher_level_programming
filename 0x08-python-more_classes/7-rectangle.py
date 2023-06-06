#!/usr/bin/python3
"""
This module includes an empty rectangle
"""


class Rectangle:
    """
    rectangle
    """

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        instanciate the rectangle with
        width and height
        """

        self.height = height
        self.width = width

    def __str__(self):
        """
        make rectangle printable as
        height by width '#'s
        """

        if self.height == 0 or self.width == 0:
            return ''

        rectangle = ''
        for i in range(self.height):
            for _ in range(self.width):
                rectangle += str(self.print_symbol)
            if i != self.height - 1:
                rectangle += '\n'

        return rectangle

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

        return self.width * self.height

    def perimeter(self):
        """
        return perimeter of rectangle
        """

        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
