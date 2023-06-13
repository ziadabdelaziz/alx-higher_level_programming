#!/usr/bin/python3
"""
append_write
"""


def append_write(filename="", text=""):
    """
    append string to file end
    """
    nb_written = 0
    with open(filename, 'a', encoding='utf-8') as file:
        nb_written = file.write(text)
    return nb_written
