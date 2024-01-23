#!/usr/bin/env python3
"""Module implements all restful api operations"""

from flask import request, jsonify, abort
from models import storage
from models.described_items import Described_item
from api.v1.blueprints import app_views
from werkzeug.datastructures import MultiDict


@app_views.route("/described_item/<string:description_id>", methods=["POST"])
@app_views.route("/described_item/<string:described_item_id>", methods=["GET", "PUT", "DELETE"])
def described_item(description_id=None, described_item_id=None):
    """Method implements all restful api operations"""
    if description_id is None and described_item_id is None:
        abort(400)
    elif description_id:
        description = storage.get("Description", description_id)
        if not prescription:
            return jsonify({"message": "invalid description_id"})
        customer_id = description.customer_id
    elif described_item_id:
        described_item = storage.get("Described_item", described_item_id)
        if not described_item:
            return jsonify({"message": "invalid described_item_id"})
        item = storage.get("Drug", described_item.item_id)
    
    if request.method == "POST":
        if "drug_id" not in request.form:
            return jsonify({"message": "drug missing"})
        elif "frequency" not in request.form:
            return jsonify({"message": "frequecy of intake missing"})
        elif "days" not in request.form:
            return jsonify({"message": "days missing"})
        else:
            new_form_data = MultiDict(request.form)
            new_form_data["description_id"] = description_id
            new_described_item = Described_item(**new_form_data)
            item = storage.get("Item", new_form_data["drug_id"])
            days = int(new_form_data["days"])
            frequency = int(new_form_data["frequency"])
            item.quantity -= (frequency * days)
            new_described_item.save()
            return jsonify(new_described_item.to_dict()), 200
    elif request.method == "PUT":
        data = request.form
        if not data:
            return
        if data["item_id"] != described_item.item_id:
            item.quantity  += int(described_item.frequency) * int(described_item.days)
            item.save()
            new_item = storage.get("Item", data["item_id"])
            new_item.quantity -= int(data["frequency"]) * int(data["days"])
            new_item.save()
        else:
            quantity = int(data["frequency"]) * int(data["days"])
            addition = (int(described_item.frequency) * int(described_item.days)) - quantity
            item.quantity += addition

        for key, value in data.items():
            if key not in ["description_id", "id", "created_at", "updated_at"]:
                setattr(described_item, key, value)
        described_item.save()
        return jsonify(described_item.to_dict()), 201
    elif request.method == "GET":
        return jsonify(described_item.to_dict()), 200
    elif request.method == "DELETE":
        item.quantity += (int(described_item.frequency) * int(described_item.days))
        item.save()
        storage.delete(described_item)
        return jsonify({})
