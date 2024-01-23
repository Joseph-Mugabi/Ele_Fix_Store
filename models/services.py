#!/usr/bin/python3

"""Module implements the Services class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class Service(BaseModel, Base):
    """Class Service provides a description of a service"""
    if models.storage_t == "db":
        __tablename__ = "services"
        name = Column(String(128), nullable=False)
        description = Column(String(256), nullable=False)
        price = Column(Integer, nullable=True)
