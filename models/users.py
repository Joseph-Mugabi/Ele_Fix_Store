#!/usr/bin/python3
"""
Class User
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relationship
from hashlib import md5

class User(UserMixin, BaseModel, Base):
    """Class implements User"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)
    #name = Column(String(128), nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(60), nullable=False)
    password = Column(String(128), nullable=False)
    contact = Column(String(60), nullable=True)
    role = Column(String(128), nullable=True)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def get_id(self):
        return str(self.id)  # Convert the user ID to string

    # Flask-Login Required Methods

    def is_authenticated(self):
        return True  # Assuming all users are authenticated

    def is_active(self):
        return True  # Assuming all users are active

    def is_anonymous(self):
        return False  # Assuming all users are not anonymous
