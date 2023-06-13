#!/usr/bin/python3
"""
load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    read a json file
    """
    obj = None

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        obj = json.loads(content)

    return obj
