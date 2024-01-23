#!/usr/bin/python3
'''
Module implements the procurement module
'''
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class Procurement(BaseModel, Base):
    """Class Procurement represents a procurement entry"""
    if models.storage_t == "db":
        __tablename__ = "procurements"
        vendor_name = Column(String(128), nullable=False)
        procurement_id = Column(String(60), nullable=False)
        drug_id = Column(String(60), ForeignKey("items.id"), nullable=False)
        name = Column(String(128), nullable=False)
        quantity = Column(Integer, nullable=False)
        price = Column(Integer, nullable=False)

        item = relationship("Item", back_populates="procurements",
                            overlaps="item_procurements")
