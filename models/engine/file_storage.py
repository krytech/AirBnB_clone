#!/usr/bin/python3
""" File storage engine. """
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to
    instances.

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return all objects. """
        return self.__objects

    def new(self, obj):
        """ Add a new object to "__objects". """
        name = obj.__class__.__name__
        id = obj.id
        key = name + '.' + id
        self.__objects.update({key: obj.to_dict()})

    def save(self):
        """ Serialize "__objects" to JSON file. """
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """ Deserialize JSON file to "__objects". """
        try:
            with open(self.__file_path) as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
