#!/usr/bin/python3
"""
this module includes
is_kind_of_class method
"""

def is_kind_of_class(obj, a_class):
    """
    check if obj is an instance of a_class
    or it's parent class
    """
    return type(obj) is a_class or type(obj) is a_class.__base__
