#!/usr/bin/env python3
import json
from models.base_model import BaseModel
"""
storage file
"""


class FileStorage:
    """store all objects in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Adds objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ save json files"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """json to file"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    if cls_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
