#!/usr/bin/pyyhon3
""" objcts  to handle all default RestFul API actions for users """

from models.items import Item
from models import storage
from api.v1.blueprints import app_views
from flask import Flask, render_template, abort, jsonify, make_response, request
from flasgger.utils import swag_from

strict_slashes = False
@app_views.route('/store', methods=['GET', "POST"])
@app_views.route('/store/<string:item_id>', methods=["GET", "PUT", "DELETE"])
def store(item_id=None):
    """all restful appi"""
    if item_id:
        item = storage.get("Item", item_id)
        if item is None:
            abort(404)
            return

    if request.method == "GET":
        if item_id is None:
            all_items = [item.to_dict() for item in
                        storage.all("Item").values()]
            return jsonify(all_items)
        return jsonify(item)

    elif request.method == "POST":
        data = request.get_json()
        if data is None:
            return jsonify({"message": "Not valid json"})
        elif "name" not in data:
            return jsonify({"message": "Item name must be specified"})
        elif "quantity" not in data:
            return jsonify({"message": "Item quantity must be specified"})
        if data["price"] == "None" or data["price"] == "" or data["price"] == None:
            del data["price"]
        if data["quantity"] == "None" or data["quantity"] == "" or data["quantity"] == None:
            del data["quantity"]
        new_item = Item(**data)
        new_item.save()
        return make_response(jsonify({"message": "Successfully created item"},
                                     new_item.to_dict()), 200)

    elif request.method == "PUT":
        data = request.get_json()
        if data is None:
            return jsonify({"message": "Not valid json"})
        if data["price"] == "None" or data["price"] == "" or data["price"] == None:
            del data["price"]
        if data["quantity"] == "None" or data["quantity"] == "" or data["quantity"] == None:
            del data["quantity"]
        for attr, value in data.items():
            if attr not in ["id", "created_at", "updated_at"]:
                setattr(item, attr, value)
        item.save()
        return make_response(jsonify({"message": "Successfully updated item"},
                                     item.to_dict()), 201)

    elif request.method == "DELETE":
        item.delete()
        storage.save()
        return jsonify({})
