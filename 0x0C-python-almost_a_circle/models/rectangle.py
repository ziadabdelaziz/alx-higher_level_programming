#!/usr/bin/python3
"""
This module includes
Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle object
    """

    __width = None
    __height = None
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Inintialization function
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        x coordinate getter
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        x coordinate setter
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        y coordinate getter
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        y cooridinate setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
