#!/usr/bin/env python3
"""Module implements described items"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Described_item(BaseModel, Base):
    """Class creates schema for described item"""
    __tablename__ = "described_items"
    item_id = Column(String(60), ForeignKey("items.id"))
    description_id = Column(String(60), ForeignKey("descriptions.id"))
    technician = Column(String(128), nullable=True)
    days = Column(Integer, nullable=False)
    item = relationship("Item", backref="described_items")
