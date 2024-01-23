#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.users import User
from models.customers import Customer  , customer_item
from models.items import Item
from os import getenv
from flask import Flask
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.deliverables import Deliverable
from models.described_items import Described_item
from models.descriptions import Description
from models.invoices import Invoice
from models.invoice_services import Invoiced_service
from models.messages import Message
from models.payments import Payment
from models.procurements import Procurement
from models.services import Service


classes = {"User": User, "Item": Item, "Customer": Customer,
           "Deliverable": Deliverable, "Description": Description,
           "Described_item": Described_item, "Invoice": Invoice,
           "Invoiced_service": Invoiced_service, "Message": Message,
           "Payment": Payment, "Procurement": Procurement,
           "Service": Service, "customer_item": customer_item}


class DB_Storage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        DSE_USER = getenv('DSE_USER')
        DSE_PWD = getenv('DSE_PWD')
        DSE_HOST = getenv('DSE_HOST')
        DSE_DB = getenv('DSE_DB')
        DSE_ENV = getenv('DSE_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(DSE_USER,
                                             DSE_PWD,
                                             DSE_HOST,
                                             DSE_DB))
        if DSE_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def create(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
        self.__session.commit()

    def update(self, key, **kwargs):
        """updates an instance"""
        obj_id = key.split(".")[1]
        class_name = key.split(".")[0]
        obj = self.__session.query(classes[class_name]).filter_by(id=obj_id).first()
        for key, value in kwargs.items():
            setattr(obj, key, value)
        self.__session.commit()

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        Session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(Session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of all objects in storage
        """
        if cls:
            return len(self.all(cls))
        return len(self.all())

        """all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count"""

    def search(self, query, cls):
        """search against a query string"""
        results = self.__session.query(classes[cls]).filter(classes[cls].name.ilike(f'%{query}')).all()
        return results

    def search_one(self, cls, **kwargs):
        """search 4 1 item based on string"""
        results = self.__session.query(classes[cls]).filter_by(**kwargs).first()
        return results

    def rollback(self):
        """rolling back"""
        self.__session.rollback()

    def search_with_customer_id(self, cls, customer_id):
        """search item based on a specific id"""
        results = self.__session.query(classes[cls]).filter_by(customer_id=customer_id).all()
        return results

    def search_with_description_id(self, cls, description_id):
        """search item based on specific id"""
        results = self.__session.query(classes[cls]).filter_by(description_id=description_id).all()
        return results

    def search_with_invoice_id(self, cls, invoice_id):
        """search items with spfic id"""
        results = self.__session.query(classes[cls]).filter_by(invoice_id=invoice_id).all()
