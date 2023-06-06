#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Add the two integers a and b
    Check first if a and b are integers or floats
    if not, raise type error
    else return integer addition
    """
    if not isinstance(a, int) or not isinstance(a, float):
        TypeError("a must be an integer")
    elif not isinstance(a, int) or not isinstance(a, float):
        TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
