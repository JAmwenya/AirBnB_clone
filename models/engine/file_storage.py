#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns the objects dictionary"""
        return FileStorage.__objects
    def new(self, obj):
        """Stores a new object"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
        self.obj = obj.__class__.__name__
    def save(self):
        """Serializes __objects to a JSON file at the specified path (__file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            object_dict = FileStorage.__objects
            my_serialized_obj = {key: obj.to_dict() for key, obj in object_dict.items()}
            json.dump(my_serialized_obj, file)


    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                team_dict = json.loads(f.read())
                for value in team_dict.values():
                    cls1_name = value["__class__"]
                    self.new(eval(cls1_name)(**value))
        except Exception:
            pass

