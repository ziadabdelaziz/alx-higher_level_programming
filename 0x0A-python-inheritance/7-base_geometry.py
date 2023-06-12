#!/usr/bin/python3
"""
Includes BaseGeometry class
"""


class BaseGeometry:
    """
    includes unimplemented method
    """

    def area(self):
        """
        raise not implemented exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
