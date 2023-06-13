#!/usr/bin/python3
"""
read_file
"""


def read_file(filename=""):
    """
    reads from filename and prints
    it's content to the stdout
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
