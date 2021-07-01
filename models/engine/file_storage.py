#!/usr/bin/python3
"""File storage engine."""
import json


class FileStorage:
    """De/serialize instances to/from a JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to "__objects"."""
        name = obj.__class__.__name__
        id = obj.id
        key = name + '.' + id
        self.__objects.update({key: obj})

    def save(self):
        """Serialize "__objects" to JSON file."""
        with open(self.__file_path, "w") as file:
            json.dump(
                {k: v.to_dict() for k, v in self.__objects.items()}, file
            )

    def reload(self):
        """Deserialize JSON file to "__objects"."""
        from ..base_model import BaseModel
        try:
            with open(self.__file_path) as file:
                self.__objects = {
                    k: BaseModel(**v) for k, v in json.load(file).items()
                }
        except FileNotFoundError:
            pass
