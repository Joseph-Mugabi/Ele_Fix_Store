#!/usr/bin/python3
'''
procurement api endpoints
'''
from flask import jsonify, make_response, request, abort
from models import storage
from models.procurements import Procurement
from models.items import Item
from api.v1.blueprints import app_views
import uuid


@app_views.route("/procurements", methods=["GET", "POST"])
@app_views.route("/procurements/<string:procurement_id>", methods=["GET", "PUT", "DELETE"])
def procurements(procurement_id=None):
    """default RESTful API actions for Procurement class"""
    if procurement_id:
        procurements = storage.all("Procurement").values()
        procurements_with_id = [procurement.to_dict() for procurement in procurements if procurement.procurement_id == procurement_id]
        if not procurements_with_id:
            abort(404)
        return jsonify(procurements_with_id)

    if request.method == "GET":
        all_procurements = [procurement.to_dict() for procurement in storage.all("Procurement").values()]
        return jsonify(all_procurements)

    elif request.method == "POST":
        data = request.get_json()
        if data is None:
            return jsonify({"message": "Not valid JSON"})

        vendor_name = data.get("vendor_name")
        item = data.get("items")

        if not vendor_name or not items or not isinstance(items, list):
            return jsonify({"message": "Invalid data format"})

        procurement_id = str(uuid.uuid4())

        created_procurements = []

        for item_data in items:
            item_name = item_data.get("name")
            quantity = int(item_data.get("quantity"))
            price = item_data.get("price")

            if not item_name or not quantity:
                return jsonify({"message": "Invalid drug data"})

            item = None
            for existing_item in storage.all("Item").values():
                if existing_item.name == item_name:
                    item = existing_item
                    break

            if item:
                item.quantity = int(item.quantity) + quantity
            else:
                item = Item(name=item_name, quantity=quantity, price=price)
                storage.create(item)
            
            procurement = Procurement(vendor_name=vendor_name, procurement_id=procurement_id, item_id=item.id, name=item_name, quantity=quantity, price=price)
            
            storage.create(procurement)

            created_procurements.append(procurement.to_dict())  # Serialize each created procurement

        storage.save()  # Save all the created objects at once

        return jsonify({"message": "Successfully created procurements", "procurements": created_procurements})

    elif request.method == "PUT":
        data = request.get_json()
        if data is None:
            return jsonify({"message": "Not valid JSON"})

        for attr, value in data.items():
            if attr not in ["id", "created_at", "updated_at"]:
                setattr(procurement, attr, value)
        storage.save()  # Save the changes to the storage
        return make_response(jsonify({"message": "Successfully updated procurement", **procurement.to_dict()}), 201)

    elif request.method == "DELETE":
        procurements = storage.all("Procurement").values()
        deleted_procurements = []

        for procurement in procurements:
            if procurement.procurement_id == procurement_id:
                deleted_procurements.append(procurement)

        items = storage.all("Item").values()
        for procurement in deleted_procurements:
            item = next((item for item in items if item.id == procurement.item_id), None)
            if item:
                item.quantity -= procurement.quantity
                storage.save(item)

        for procurement in deleted_procurements:
            storage.delete(procurement)

        storage.save()  # Save the changes to the storage

        return jsonify({"message": "Deleted successfully!"})
