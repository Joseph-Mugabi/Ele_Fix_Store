#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request, abort
from models import storage, storage_t
from models.services import Service
from api.v1.blueprints import app_views

@app_views.route("/services", methods=["GET", "POST"])
@app_views.route("/services/<string:service_id>", methods=["GET", "PUT", "DELETE"])
def services(service_id=None):
    """Handles all default RESTful API actions for Service class"""
    if service_id:
        service = storage.get("Service", service_id)
        if service is None:
            abort(404)

    if request.method == "GET":
        if service_id is None:
            all_services = [service.to_dict() for service in
                            storage.all("Service").values()]
            return jsonify(all_services)
        return jsonify(service.to_dict()) # service object to json(serialization)

    elif request.method == "POST":
        data = request.get_json()
        if data is None:
            return jsonify({"message": "Not valid JSON"})
        elif "name" not in data:
            return jsonify({"message": "Service name must be specified"})
        elif "description" not in data:
            return jsonify({"message": "Service description must be specified"})

        new_service = Service(**data)
        new_service.save()
        return make_response(jsonify({"message": "Successfully created service"},
                                     new_service.to_dict()), 200)

    elif request.method == "PUT":
        data = request.get_json()
        if data is None:
            return jsonify({"message": "Not valid JSON"})

        for attr, value in data.items():
            if attr not in ["id", "created_at", "updated_at"]:
                setattr(service, attr, value)
        service.save()
        return make_response(jsonify({"message": "Successfully updated service"},
                                     service.to_dict()), 201)

    elif request.method == "DELETE":
        service.delete()
        storage.save()
        return jsonify({"message": "Deleted Successfully!"})
