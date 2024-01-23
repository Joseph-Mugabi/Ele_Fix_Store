#!/usr/bin/python3

"""Module handles all api actions for customers_drugs relationship"""

from flask import Flask, jsonify, request, make_response, abort
from models.customers import Customer
from models.items import Item
from models import storage
from models import storage_t
from api.v1.blueprints import app_views


@app_views.route("/customer/<string:customer_id>/item", methods=["GET"])
@app_views.route("/customer/<string:customer_id>/item/<string:item_id>", methods=["POST", "DELETE"])
def customer_item(customer_id, item_id=None):
    """ api actions for customers_items relationship"""
    if customer_id is None:
        return
    
    customer = storage.get("Customer", customer_id)
    if customer is None:
        abort(404)
        return

    if item_id:
        item = storage.get("Item", item_id)
        if item is None:
            abort(404)
            return

    customer = storage.get("Customer", customer_id)

    customer_items = customer.items

    if request.method == "GET":
        return jsonify([item.to_dict() for item in customer_items])

    elif request.method == "POST":
        if item in customer_items:
            item.quantity -= 1
            customer_items.append(item)
            item.save()
            customer.save()
            item = storage.get("Item", item_id)
            return jsonify(item.to_dict())
        customer_items.append(item)
        item.quantity -= 1
        item.save()
        customer.save()
        item = storage.get("Item", item_id)
        return jsonify(item.to_dict())

    elif request.method == "DELETE":
        customer_items.remove(item)
        storage.save()
        return jsonify({})
