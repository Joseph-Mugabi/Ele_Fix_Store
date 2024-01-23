#!/usr/bin/python3

"""Modules implements tests for customer class"""

import unittest
import inspect
from models.customers import Customer
from models.item import Item
from models.payments import Payment
from models import storage
from models.base_model import BaseModel
import pep8 as pycodestyle
module_doc = customers.__doc__


class test_customer(unittest.TestCase):
    """class implements tests for customer class"""
    @classmethod
    def setUpClass(self):
        """set up any resources or objects that are needed for the tests"""
        self.all_methods = inspect.getmembers(Customer, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """Tests styling compliance"""
        paths = ["models/customers.py", "tests/tests_models/test_customers.py"]
        for path in paths:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)
