#!/usr/bin/python3
"""
write_file
"""


def write_file(filename="", text=""):
    """
    write to file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
