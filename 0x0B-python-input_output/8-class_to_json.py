#!/usr/bin/python3
"""
class_to_json
"""
import json


def class_to_json(obj):
    """
    class to json
    """
    return json.dumps(vars(obj))
 