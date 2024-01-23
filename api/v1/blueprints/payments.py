#!/usr/bin/python3
"""all default RESTful API actions for Payment class"""

from flask import Flask, jsonify, request, make_response, abort
from models.payments import Payment
from api.v1.blueprints import app_views
from models import storage


@app_views.route("/payments/<string:customer_id>/<string:invoice_id>", methods=["GET", "POST"])
@app_views.route("/payment/<string:payment_id>", methods=["GET", "PUT", "DELETE"])
def payments(payment_id=None, customer_id=None, invoice_id=None):
    """default RESTful API actions for Payment class"""
    if payment_id:
        payment = storage.get("Payment", payment_id)
        if payment is None:
            abort(404)
            return
    if customer_id:
        customer = storage.get("Customer", customer_id)
        if customer is None:
            abort(404)
            return

    if request.method == "GET":
        if payment_id is None:
            all_payments = [payment.to_dict() for payment in
                            storage.all("Payment").values()]
            return jsonify(all_payments)
        return jsonify(payment.to_dict())

    elif request.method == "POST":
        data = request.get_json()
        if data is None:
            return jsonify({"message": "Not valid JSON"})
        if data["paid"] == "None" or data["paid"] == "" or data["paid"] == 0:
            data["paid"] = 0
        data["customer_id"] = customer.id
        data["invoice_id"] = invoice_id
        new_payment = Payment(**data)
        new_payment.save()
        pay = storage.get("Payment", new_payment.id)
        return make_response(jsonify({"message": "successfully added"},
                                     pay.to_dict(), 201))

    elif request.method == "PUT":
        data = request.get_json()
        if data is None:
            return jsonify({"message": "Not valid JSON"})
        for attr, value in data.items():
            if attr not in ["id", "created_at", "updated_at"]:
                setattr(payment, attr, value)
        payment.save()
        return make_response(jsonify({"message": "successfully updated"},
                                     payment.to_dict(), 200))

    elif request.method == "DELETE":
        payment.delete()
        storage.save()
        return jsonify({})
