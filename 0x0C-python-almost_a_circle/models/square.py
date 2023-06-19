#!/usr/bin/python3
"""
This module includes the rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization function
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overriding string representation
        """

        representation = f"[Square] ({self.id}) {self.x}/{self.y} "\
            + f"- {self.width}"

        return representation
