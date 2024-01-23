#!/usr/bin/python3

"""
Module implements invoice functionality
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.items import Item


class Invoice(BaseModel, Base):
    """implemts invoice shema"""
    __tablename__ = "invoices"
    customer_id = Column(String(60), ForeignKey("customers.id"))
    description_id = Column(String(60),
                            ForeignKey("descriptions.id"), nullable=True)
    description = relationship("Description", backref="descriptions")
    customer = relationship("Customer", back_populates="invoices",
                            overlaps="invoices")
    invoiced_services = relationship("Invoiced_service")
    payments = relationship("Payment", back_populates="invoice")
