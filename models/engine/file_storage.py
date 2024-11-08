#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
import models
from models.base_model import BaseModel
from models.customers import Customer
from models.items import Item
from models.users import User
from models.payments import Payment
from models.services import Service
from models.procurements import Procurement
from datetime import datetime
# from hashlib import md5

classes = {"User": User, "Item": Item, "Customer": Customer,
           "Procurement": Procurement, "Service": Service, "Payment": Payment}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    __file = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def create(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def new(self, obj):
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            if key == "password":
                json_objects[key].decode()
            json_objects[key] = self.__objects[key].to_dict(save_fs=1)
        with open(self.__file, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except Exception:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def update(self, obj_id, **kwargs):
        """updates instance attri"""
        try:
            if obj_id in self.__objects and kwargs:
                obj = self.__objects[obj_id]
                obj_id = obj.to_dict()
                obj_dict.update(**kwargs)
                obj = eval(obj_dict["__class__"])(**obj_dict)
                self.create(obj)
                self.save()
        except Exception:
            pass

    def get_item_by_name(self, item_name):
        """retrieves an item object by its name"""
        for item in self.__objects.valves():
            if isinstanace(item, Item) and item.name == item_name:
                return item
        return None

    def search_one(self, cls, attribute_name, attribute_value):
        """Search for the first object of a specific class with a matching attribute value."""
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        for obj in all_cls.values():
            if hasattr(obj, attribute_name) and getattr(obj, attribute_name) == attribute_value:
                return obj

        return None
    