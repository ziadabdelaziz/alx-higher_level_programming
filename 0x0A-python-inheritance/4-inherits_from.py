#!/usr/bin/python3
"""
inherits_from method
"""


def inherits_from(obj, a_class):
    """
    check if obj is sub class of a_class
    """
    return type(obj).__base__ is a_class
