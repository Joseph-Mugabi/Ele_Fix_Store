#!/usr/bin/python3
"""module entry point to API"""


from flask import Flask, jsonify, request
from models.user import User
from models.engine import db_storage

app = Flask(__name__)
storage = db_storage.DB_Storage()

strict_slashes=False
@app.route('/users', methods=['GET'])
def get_all_users():
    users = storage.all(User)
    return jsonify(users.to_dict)

@app.route('/users/<string:id>', methods=['GET'])
def get_user_by_id(id):
    obj = storage.get(id)
    if obj:
        return jsonify(obj.to_dict)
    else:
        return jsonify({'error': 'user not found'})

@app.route('/users', methods=['POST'])
def create_user():
    # Get data from request body
    data = request.json
    
    # Create a new User object
    user = User(**data)

    if not user:
        return jsonify({'error': 'ivvalid request data'})
    obj = storage.create(user)

    # Save the User object to the database
    storage.new(obj)
    storage.save()
    
    # Return the created User object as a JSON response
    return jsonify(obj.to_dict()), 201

@app.route('/users/<string:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    if not data:
        return jsonify({'error': 'invalid request data'})
    obj = storage.update(id, data)
    if obj:
        return jsonify(obj.to_dict)
    else:
        return jsonify({'error': 'object not found'})
    
@app.route('/users/<string:id>', methods=['DELETE'])
def del_user(id):
    obj = stoeage.delete(id)
    if obj:
        return jsonify(obj.to_dict)
    else:
        return jsonify({'error': 'object not found'})

if __name__ == '__main__':
    """application"""
    app.run(host="0.0.0.0", port= 5002, threaded=True)
