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

    def area(self):
        """
        calculate the area of rectangle
        """

        return self.width * self.height

    def display(self):
        """
        print the rectangle of "#"s
        to stdout
        """

        for i in range(self.height + self.y):
            if i < self.y:
                print()
                continue
            for j in range(self.width + self.x):
                if j < self.x:
                    print(end=" ")
                else:
                    print(end="#")
            print()

    def update(self, *args, **kwargs):
        """
        update the rectangle attributes
        """

        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and len(args):
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
                else:
                    break
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        return dictionary representation of
        the rectangle
        """

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }

    def __str__(self):
        """
        Edit str method
        to return rectangle id, (x, y) coordinates
        width and height
        """

        representation = f"[Rectangle] ({self.id}) {self.x}/{self.y} "\
            + f"- {self.width}/{self.height}"

        return representation
