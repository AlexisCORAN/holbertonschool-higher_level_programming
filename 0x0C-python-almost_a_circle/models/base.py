#!/usr/bin/python3
"""
This module defines the Base class
"""
import json
from os import path


class Base:
    """Representation of Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_dictionaries = []
        if list_objs is None:
            with open(filename, mode="w") as f:
                f.write(cls.to_json_string(list_dictionaries))
            return
        else:
            for i in list_objs:
                list_dictionaries.append(i.to_dictionary())
            with open(filename, mode="w") as f:
                f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) is 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode="r") as f:
            ob = cls.from_json_string(f.read())
            instances = []
            for elem in ob:
                instances.append(cls.create(**elem))

            return (instances)
