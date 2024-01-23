#!/usr/bin/pyyhon3
""" objcts  to handle all default RestFul API actions for users """

from models.users import User
from models import storage
from api.v1.blueprints import app_views
from flask import abort, jsonify, make_response, request, redirect, session
from api.v1.auth import Auth

Auth = Auth()

@app_views.route("/register", methods=["POST"])
def register_user() -> str:
    """Registers new user"""
    try:
        name = request.form.get("name")
        gender = request.form.get("gender")
        email = request.form.get("email")
        password = request.form.get("password")
        age = request.form.get("age", None)
        contact = request.form.get("contact", None)
        location = request.form.get("location", None)
        role = request.form.get("role", None)
    except KeyError:
        abort(400)
    
    try:
        user = Auth.register_user(name=name, age=age, gender=gender, email=email, password=password, contact=contact, role=role)
    except ValueError:
        return jsonify({"response": "email already registered"})
    
    return jsonify({"email": user.email, "message": "user created"})


@app_views.route("/login", methods=["POST"])
def log_in() -> str:
    """Logs in user"""
    try:
        email = request.form.get("email")
        password = request.form.get("password")
    except KeyError:
        abort(400)
    
    if not Auth.valid_login(email, password):
        abort(401)
    
    session_id = Auth.create_session(email)
    session["session_id"] = session_id
    response = jsonify({"email": email, "message": "logged in", "session_id": session_id})
    response.set_cookie("session_id", session_id)
    return response
    

@app_views.route("/logout", methods=["DELETE"])
def log_out() -> str:
    """Logs user out"""
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(403)
    
    try:
        user = Auth.retrieve_user_by_session_id(session_id)
    except Exception:
        abort(403)
    
    Auth.destroy_session(user.email)
    return redirect("/")


@app_views.route("/reset_password", methods=["POST"])
def reset() -> str:
    """Resets password"""
    try:
        email = request.form.get("email")
    except KeyError:
        raise ValueError
    
    reset_token = Auth.password_reset_token(email)
    return jsonify(reset_token)


@app_views.route("/update_password", methods=["POST"])
def update_password() -> str:
    """Updates password"""
    try:
        email = request.form.get("email")
        reset_token = request.form.get("reset_token")
        password = request.form.get("password")
    except KeyError:
        abort(400)

    try:
        Auth.update_password(reset_token, password)
    except ValueError:
        abort(403)

    return jsonify( {"email": email, "message": "Password updated"}), 200


@app_views.route("profile")
def profile():
    """Returns user profile based on email"""
    try:
        session_id = request.cookies.get("session_id")
    except KeyError:
        abort(401)
    
    user = Auth.retrieve_user_by_session_id(session_id)
    
    if not user:
        abort(403)
    
    message = {"name": user.name, "age": user.age, "gender": user.gender, "email": user.email,
               "contact": user.contact, "role": user.role}
    return jsonify(message), 200
