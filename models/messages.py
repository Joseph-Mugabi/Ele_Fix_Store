#!/usr/bin/env python3

"""Module implement message schema"""

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Message(BaseModel, Base):
    """Class implements message schema"""
    __tablename__ = "messages"
    content = Column(String(255))
    sender = Column(String(128))
