#!/usr/bin/python3
"""
class BaseModel implements all common functionality amongst classes
"""

import models
from os import getenv
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    if models.storage_t == "db":
        __tablename__ = ''
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.to_dict)

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.to_dict())

    def create(self):
        """set object in all objects dictionary"""
        models.storage.create(self)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    """def to_dict(self, save_fs=None):
        Returns a dictionary containing all keys/values of the instance.
        new_dict = self.__dict__.copy()
    
        # Safely handle the 'created_at' attribute
        if "created_at" in new_dict and new_dict["created_at"] is not None:
            new_dict["created_at"] = new_dict["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
    
        # Safely handle the 'updated_at' attribute
        if "updated_at" in new_dict and new_dict["updated_at"] is not None:
            new_dict["updated_at"] = new_dict["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
    
        new_dict["__class__"] = self.__class__.__name__
    
        # Mask the password if it exists
        if 'password' in new_dict:
            new_dict['password'] = "*" * len(new_dict['password'])
    
        # Remove SQLAlchemy internal state if present
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]

        # Optionally remove the password field when save_fs is None
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
    
        return new_dict"""

    
    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_dict["__class__"] = self.__class__.__name__
        if 'password' in new_dict:
            new_dict['password'] = "*" * len(new_dict['password'])
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]

        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
