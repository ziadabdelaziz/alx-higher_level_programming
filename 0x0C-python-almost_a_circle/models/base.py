#!/usr/bin/python3
"""
This module includes the base class
"""
import json


class Base:
    """
    The base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization function
        assign the id of the object if provided
        otherwise assign with the next object number
        """

        if id:
            self.id = id
        else:
            Base.nb_objects = self.nb_objects + 1
            self.id = self.nb_objects

    @property
    def nb_objects(self):
        """
        getter function of nb_objects
        private attribute (number of objects)
        """

        return self.__nb_objects

    @nb_objects.setter
    def nb_objects(self, value):
        """
        number of objects setter
        """

        if not isinstance(value, int):
            raise TypeError("Error: value must be an integer")
        else:
            self.__nb_objects = value

    def to_json_string(list_dictionaries):
        """
        return json representation
        of list_dictionaries
        """

        if list_dictionaries and len(list_dictionaries):
            return json.dumps(list_dictionaries)
        else:
            return "[]"
