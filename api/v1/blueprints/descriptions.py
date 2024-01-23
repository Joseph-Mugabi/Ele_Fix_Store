#!/usr/bin/env python3
"""
Module implements all prescriptions restful API routes
"""

from flask import Flask, request, abort, jsonify
from models import storage
from models.descriptions import Description
from api.v1.blueprints import app_views

@app_views.route('/descriptions/<string:customer_id>', methods=["POST"])
@app_views.route('/description/<string:description_id>', methods=["GET", "DELETE"])
def descriptions(customer_id=None, description_id=None):
    """handles all restful api operations"""
    if not customer_id and not description_id:
        return jsonify({"message": "error"})
    if request.method == "POST":
        customer = storage.get("Customer", customer_id)
        if not customer:
            return jsonify({"message": "error"})
        obj = Description(customer_id=customer_id)
        obj.save()
        storage.save()
        return jsonify(obj.to_dict()), 200
    elif request.method == "GET":
        description = storage.get("Description", description_id)
        if not description:
            return jsonify({"message": "invalid description id"})
        return jsonify(description.to_dict()), 200
    elif request.method == "DELETE":
        description = storage.get("Description", description_id)
        storage.delete(description)
        return jsonify("{}")
