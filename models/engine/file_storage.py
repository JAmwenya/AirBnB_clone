#!/usr/bin/python3
import json
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
        self.obj = obj.__class.__name
    def save(self):
        with open ("_file_path", "w") as file:
            json.dump(self.__object, file)


    def reload(self):
        with open(self.__file_path, "r") as file:
            try:
                self.__objects = json.load(file)
                return "{}".format(self.__objects)
        except json.JSONDecodeError:
            return "Error decoding JSON data"

      

