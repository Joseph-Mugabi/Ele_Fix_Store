#!/usr/bin/python3
""" Class customers"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import MetaData, Column, String, Table, Integer, ForeignKey, Text, text
from sqlalchemy.orm import relationship
from os import getenv
import uuid


# define customer item table
# metadata = MetaData()
"""
if models.storage_t == "db":
    customer_item = Table("customers_items", Base.metadata,
                        Column("customer_id", String(60), ForeignKey("customers.id")),
                        Column("item_id", String(60), ForeignKey("items.id")))
"""
#customer_item = Table(
#    "customers_items",
#    Base.MetaData(),
#    Column("customer_id", String(60), ForeignKey("customers.id")),
#    Column("item_id", String(60), ForeignKey("items.id"))
#)


# if models.storage_t == "db":
class Customer(BaseModel, Base):
    """representation of customer clss"""
    __tablename__ = 'customers'
    name = Column(String(128), nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(60), nullable=False)
    address = Column(String(60), nullable=False)
    email = Column(String(128), nullable=True)
    contact = Column(String(60), nullable=False)
    payments = relationship("Payment", backref="customer",
                            cascade="all, delete")
    #items = relationship("Item", secondary="customers_items", backref="customers", viewonly=False)
    #items = relationship("Item", secondary="customers_items",
    #                     backref="customer_items", viewonly=False)
    descriptions = relationship("Description", back_populates="customer",
                                overlaps="descriptions")
    deliverables = relationship("Deliverable", back_populates="customer",
                                overlaps="deliverables")
    invoices = relationship("Invoice", back_populates="customer",
                            overlaps="invoices")
    
    if models.storage_t != "db":
        @property
        def items(self):
            """methd retrns all items described for a customer"""
            from models.items import Item
            item_list = []
            for item in models.storage.all(Item).values():
                if item.customer_id == self.id:
                    item_list.append(item)
            return item_list

        @property
        def payments(self):
            """retrns all paymts per/customer"""
            from models.payments import Payment
            payment_list = []
            for Payment in models.storage.all(Payment).values():
                if Payment.customer_id == self.id:
                    payment_list.append(Payment)
            return payment_list
