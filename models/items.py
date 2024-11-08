#!/usr/bin/python3
""" Class items"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Text, text
from os import getenv
from sqlalchemy.orm import relationship
#from models.customers import customer_item 


class Item(BaseModel, Base):
    """ representation of item clss"""
    if models.storage_t == "db":
        __tablename__ = 'items'
        name = Column(String(128), nullable=False)
        quantity = Column(Integer, nullable=False, default=0)
        price = Column(Integer, nullable=True)

        procurements = relationship("Procurement", backref="item_procurements")
        #customers = relationship('Customer', back_populates='items')
        #customer = relationship("Customer", secondary=customer_item, back_populates="items")
