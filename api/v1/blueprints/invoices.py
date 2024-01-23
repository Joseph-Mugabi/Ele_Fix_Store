#!/usr/bin/env python3
"""Module implements all invoices restful api operations"""

from flask import Flask, request, jsonify, abort
from models import storage
from models.invoices import Invoice
from api.v1.blueprints import app_views


@app_views.route("/invoices/<string:customer_id>", methods=["POST"])
@app_views.route("/description_invoice/<string:description_id>", methods=["POST"])
@app_views.route("/invoice/<string:invoice_id>", methods=["GET", "PUT", "DELETE"])
def invoices(customer_id=None, invoice_id=None, description_id=None):
    """implements all restful api operations"""
    if customer_id is None and invoice_id is None and description_id is None:
        abort(400)
    if customer_id:
        customer = storage.get("Customer", customer_id)
        if customer is None:
            abort(404)
    elif invoice_id:
        invoice = storage.get("Invoice", invoice_id)
        if invoice is None:
            return
    elif description_id:
        description = storage.get("Description", description_id)
        if description is None:
            return
    if request.method == "POST":
        if description_id:
            customer_id = description.customer_id
            new_invoice = Invoice(description_id=description_id, customer_id=customer_id)
        elif customer_id:
            new_invoice = Invoice(customer_id=customer_id)
        new_invoice.save()
        return jsonify(new_invoice.to_dict()), 201
    elif request.method == "GET":
        return jsonify(invoice.to_dict()), 200
    elif request.method == "DELETE":
        storage.delete(invoice)
        return jsonify({})
    elif request.method == "PUT":
        data = request.get_json()
        if not data:
            return jsonify({"message": "data not submitted"})
        else:
            for key, value in data.values():
                if key not in ["id", "created_at", "updated_at"]:
                    setattr(invoice, key, value)
            invoice.save()
            return jsonify(invoice.to_dict()), 200
