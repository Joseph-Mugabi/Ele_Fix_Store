#!/usr/bin/env python3
"""Module implements Descriptions table"""

from sqlalchemy import Column, String, Integer, Date, ForeignKey, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models.described_items import Described_item


class Description(BaseModel, Base):
    """Class implements description"""
    __tablename__ = "descriptions"
    customer_id = Column(String(60), ForeignKey("customers.id"))
    described_items = relationship("Described_item")
    customer = relationship("Customer", back_populates="descriptions",
                            overlaps="descriptions")
