#!/usr/bin/python3
"""
This module includes the base class
"""
import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return json representation
        of list_dictionaries
        """

        if list_dictionaries and len(list_dictionaries):
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write json representation of instances
        to file
        """

        file_name = f"{cls.__name__}.json"
        list_dictionaries = []
        if list_objs is not None:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]

        list_json = Base.to_json_string(list_dictionaries)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(list_json)

    @staticmethod
    def from_json_string(json_string):
        """
        return json representation of
        json string
        """

        if json_string and len(json_string):
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        return Rectangle instance
        from dictionary
        """

        instance = None
        if cls.__name__ == "Rectangle":
            instance = cls(2, 1)
        else:
            instance = cls(1)

        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        return an instances of cls
        from json file
        """

        file_string = None
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                file_string = file.read()
        except FileNotFoundError:
            return []

        list_objs = cls.from_json_string(file_string)

        list_instances = list()
        for obj in list_objs:
            list_instances.append(cls.create(**obj))

        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        saves list of objects
        to csv file
        """

        file_name = f"{cls.__name__}.csv"

        list_dictionaries = []
        if list_objs is not None:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]

        keys = list_dictionaries[0].keys()
        with open(file_name, 'w', encoding="utf-8", newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(list_dictionaries)

    @classmethod
    def load_from_file_csv(cls):
        """
        load objects from csv file
        """

        file_name = f"{cls.__name__}.csv"
        list_instances = []
        try:
            with open(file_name, 'r', encoding='utf-8', newline='\n') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(value)
                    list_instances.append(cls.create(**row))
        except FileNotFoundError:
            return list_instances

        return list_instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draw a list of rectangles and squares
        """

        turtle.penup()
        for shape in list_rectangles + list_squares:
            turtle.goto(shape.x, shape.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(shape.width)
                turtle.right(90)
                turtle.forward(shape.height)
                turtle.right(90)
            turtle.penup()

        turtle.done()
