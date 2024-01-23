#!/usr/bin/python3
"""Module runs tests on BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
import inspect
import pep8 as pycodestyle
module_doc = models.base_model.__doc__


class Test_BaseModel_docs(unittest.TestCase):
    """Tests the documentation of the BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Retrieve all BaseModel methods"""
        self.base_attr = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """test proper styling """
        for path in ["models/base_model.py",
                     "tests/test_models/test_base_model.py"]:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstrings(self):
        """Test module  documentation"""
        self.assertIsNot(module_doc, None, "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1, "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test class documentation"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class requires documentation")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class requires documentation")

    def test_methods_docstring(self):
        """Test method documentation"""
        for method in self.base_attr:
            self.assertIsNot(method[1].__doc__, None,
                             "Documentation required for {}".format(method[0]))
            self.assertTrue(len(method[1].__doc__) >= 1,
                            "Documentation required for {}".format(method[0]))


class Test_BaseModel(unittest.TestCase):
    """Tests the basemodel class"""
    def test_create(self):
        """Checks instantiation and assignment of
           attributes to BaseModel object"""
        inst = BaseModel()
        assert isinstance(inst, BaseModel)

        inst.name = "base"
        inst.age = 20
        assert hasattr(inst, "name")
        assert getattr(inst, "name") == "base"
        assert getattr(inst, "age") == 20

        all_attr = {"id": str, "updated_at": datetime,
                    "created_at": datetime, "name": str, "age": int}

        for attr, typ in all_attr.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, inst.__dict__)
                self.assertIs(type(inst.__dict__[attr]), typ)

    def test_time(self):
        """checks behaviour of created at and updated at"""
        inst = BaseModel()

        assert isinstance(inst.created_at, datetime)
        assert isinstance(inst.updated_at, datetime)
        self.assertEqual(inst.created_at, inst.updated_at)

        old_time = inst.updated_at

        inst.name = 'base'
        inst.save()

        new_time = inst.updated_at
        self.assertNotEqual(old_time, new_time)

    def test_to_dict(self):
        """checks dictionary representation of object"""
        inst = BaseModel()
        inst.name = "base"

        inst_dict = inst.to_dict()
        self.assertIs(type(inst_dict), dict)

        expected_attr = ["id", "created_at", "updated_at",
                         "__class__", "name"]

        for attr in expected_attr:
            self.assertIn(attr, inst.to_dict())

    def test_uuid(self):
        """Test id attribute of BaseModel Object"""
        inst = BaseModel()
        inst2 = BaseModel()

        self.assertNotEqual(inst.id, inst2.id)
        assert isinstance(inst, uuid)
