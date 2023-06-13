#!/usr/bin/python3
"""
save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write object to text file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        writable = json.dumps(my_obj)
        file.write(writable)
