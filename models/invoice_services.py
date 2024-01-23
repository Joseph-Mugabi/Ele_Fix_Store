#!/usr/bin/env python3
"""Module implements invoice services"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Invoiced_service(BaseModel, Base):
    """Class creates schema for invoiced services"""
    __tablename__ = "invoiced_services"
    invoice_id = Column(String(60), ForeignKey("invoices.id"))
    service_id = Column(String(60), ForeignKey("services.id"))
    service = relationship("Service", backref="invoiced_services")
