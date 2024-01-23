#!/usr/bin/python3
"""Implements tests for Item Class"""
import unittest
from models import storage
from models.items import Item
from models.customers import Customer
from models.customers_items import CustomerItem
from models import storage_env
from api.v1.views import ui
from flask import Flask, jsonify, request, make_response, abort
from api.v1.views.customers_items import customer_item

class TestItem(unittest.TestCase):
    """Tests Item Class"""
    def setUp(self):
        """Sets up test environment"""
        self.app = Flask(__name__)
        self.app.register_blueprint(ui)
        self.client = self.app.test_client()

    def test_get_customer_items(self):
        """Tests GET /customer/<customer_id>/item"""
        customer = Customer()
        customer.save()
        item = Item()
        item.save()
        customer_item = CustomerItem()
        customer_item.customer_id = customer.id
        customer_item.item_id = item.id
        customer_item.save()
        response = self.client.get("/api/v1/customer/{}/item".format(customer.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [item.to_dict()])

    def test_post_customer_item(self):
        """Tests POST /customer/<customer_id>/item/<item_id>"""
        customer = Customer()
        customer.save()
        item = Item()
        item.save()
        response = self.client.post("/api/v1/customer/{}/item/{}".format(customer.id, item.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, item.to_dict())

    def test_delete_customer_item(self):
        """Tests DELETE /customer/<customer_id>/item/<item_id>"""
        customer = Customer()
        customer.save()
        item = Item()
        item.save()
        customer_item = CustomerItem()
        customer_item.customer_id = customer.id
        customer_item.item_id = item.id
        customer_item.save()
        response = self.client.delete("/api/v1/customer/{}/item/{}".format(customer.id, item.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {})

    def tearDown(self):
        """Tears down test environment"""
        storage.delete_all(storage_t)

    def test_create_item(self):
        """Tests Item creation"""
        item = Item()
        item.name = "Test Item"
        item.save()
        self.assertEqual(item.name, "Test Item")

    def test_attributes(self):
        """Tests Item attributes"""
        item = Item()
        item.name = "Test Item"
        item.save()
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.id, item.id)
        self.assertEqual(item.created_at, item.created_at)
        self.assertEqual(item.updated_at, item.updated_at)

    def test_to_dict(self):
        """Tests Item to_dict"""
        item = Item()
        item.name = "Test Item"
        item.save()
        self.assertEqual(item.to_dict()["name"], "Test Item")
        self.assertEqual(item.to_dict()["id"], item.id)
        self.assertEqual(item.to_dict()["created_at"], item.created_at.isoformat())
        self.assertEqual(item.to_dict()["updated_at"], item.updated_at.isoformat())

    def test_str(self):
        """Tests Item __str__"""
        item = Item()
        item.name = "Test Item"
        item.save()
        self.assertEqual(str(item), "[Item] ({}) {}".format(item.id, item.__dict__))

