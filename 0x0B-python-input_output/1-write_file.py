#!/usr/bin/python3
"""
write_file
"""


def write_file(filename="", text=""):
    """
    write to file
    """
    nb_written = 0
    with open(filename, 'w', encoding='utf-8') as file:
        nb_written = file.write(text)
    return nb_written