#!/usr/bin/python3
"""
Class User
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relationship
from hashlib import md5
from flask_login import UserMixin
from werkzeug.security import check_password_hash


class User(BaseModel, UserMixin, Base):
    """the representation of a class  User"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        name = Column(String(128), nullable=False)
        age = Column(Integer, nullable=True)
        gender = Column(String(60), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        location = Column(String(128), nullable=True)
        contact = Column(String(60), nullable=True)
        role = Column(String(128), nullable=True)
        session_id = Column(String(256))
        reset_token = Column(String(256))

    else:
        name = ""
        email = ""
        password = ""
        location = ""
        contact = ""

    def __init__(self, *args, **kwargs):
        """ Initialisation of the User"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return str(self.id)  # convt user id to string

    # flash login needs methods

    def is_authenticated(self):
        return True  # assume all users are authenticated

    def is_active(self):
        return True  # assume all users are active

    def is_anonymous(self):
        return False  # assume all users are not anonymous
