#!/usr/bin/pyyhon3
""" objcts  to handle all default RestFul API actions for settings """

from flask import request, jsonify, abort
from models import storage
from models.invoice_services import Invoiced_service
from api.v1.blueprints import app_views
from models.invoices import Invoice


@app_views.route("/invoice_services", methods=["POST"])
@app_views.route("/invoice_service/<string:id>", methods=["GET", "PUT", "DELETE"])
def invoice_services(id=None):
    """Handles endpoints for invoice services"""
    if id:
        service_invoiced = storage.get("Invoiced_services", id)
    
    if request.method == "POST":
        data = request.form
        if not data:
            abort(403)
        if "invoice_id" not in data:
            return jsonify({"message": "include invoice id"})
        elif "service_id" not in data:
            return jsonify({"message": "must include service_id"})
        else:
            new_invoice_service = Invoiced_services(**data)
            new_invoice_service.save()
            return jsonify(new_invoice_service.to_dict()), 200
    elif request.method == "PUT":
        data = request.form
        if not data:
            abort(403)
        if "invoice_id" not in data:
            return jsonify({"message": "include invoice id"})
        elif "service_id" not in data:
            return jsonify({"message": "must include service_id"})
        else:
            for key, value in data.items():
                if key not in ["id", "created_at", "updated_at"]:
                    setattr(service_invoiced, key, value)
            service_invoiced.save()
            return jsonify(service_invoiced.to_dict()), 201
    elif request.method == "GET":
        if id:
            return jsonify(service_invoiced.to_dict()), 200
        else:
            all_services_invoiced = [ item.to_dict() for item in storage.all("Invoiced_services").values() ]
            return jsonify(all_services_invoiced), 200
    elif request.method == "DELETE":
        storage.delete(service_invoiced)
        return jsonify({})

@app_views.route("/create_invoice", methods=["POST"])
def invoice_created():
    """adds new service and new invoice"""
    invoice = Invoice()