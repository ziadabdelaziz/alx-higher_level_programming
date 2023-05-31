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

    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiate 'size' and position attributes safely
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter function for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter function for position
        """
        if not isinstance(value, tuple) or not len(value) == 2\
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        print square of '#' with side equals 'size'
        """
        for _ in range(self.position[1]):
            print()

        if self.size == 0:
            print()
            return

        for _ in range(self.size):
            for i in range(self.size + self.position[0]):
                if i < self.position[0]:
                    print(end=' ')
                else:
                    print("#", end='')
            print()
