#!/usr/bin/python3
""" customer"""

import models
from models.base_model import BaseModel
from models.customers import Customer
from models import storage, storage_t
from api.v1.blueprints import app_views
from flask import Flask, abort, make_response, request, jsonify

strict_slashes=False

@app_views.route('/status', methods=['GET'])
def status():
    """ status of APIA """
    return jsonify({'Status': 'OK'})

@app_views.route("/customers", methods=["GET", "POST"])
@app_views.route("/customers/<string:customer_id>", methods=["GET", "PUT", "DELETE"])
def customers(customer_id=None):
    """all default RESTful API actions for customer object"""
    if customer_id:
        customer = storage.get("Customer", customer_id)
        if not customer:
            abort(404)
            return

    if request.method == "GET":
        if customer_id:
            return jsonify(customer.to_dict())
        all_customers = [obj.to_dict() for obj in
                        storage.all("Customer").values()]
        return jsonify(all_customers)

    elif request.method == "POST":
        if request.get_json() is None:
            return jsonify({"message": "Not valid json"})
        elif "name" not in request.get_json():
            return jsonify({"message": "name must be specified"})
        elif "gender" not in request.get_json():
            return jsonify({"message": "gender must be specified"})

        attr = request.get_json()
        if attr["contact"] == "None" or attr["contact"] == "":
            del attr["contact"]
        if attr["age"]  == "None" or attr["age"] == "" or attr["age"] == 0:
            del attr["age"]
        obj = Customer(**attr)
        obj.save()
        pt = storage.get("Customer", obj.id)
        return make_response(jsonify(pt.to_dict()), 201)

    elif request.method == "PUT":
        if request.get_json() is None:
            return jsonify({"message": "Not valid json"})
        attr = request.get_json()
        if attr["contact"] == "None" or attr["contact"] == "":
            del attr["contact"]
        if attr["age"] == "None" or attr["age"] == "" or attr["age"] == 0:
            del attr["age"]
        for key, value in attr.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(customer, key, value)
        customer.save()
        cust = storage.get("Customer", customer.id)
        return make_response(jsonify(cust.to_dict()), 200)

    elif request.method == "DELETE":
        customer.delete()
        storage.save()
        return (jsonify({}))
