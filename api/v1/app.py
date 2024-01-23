#!/usr/bin/python3
""" Flask Application """

from models import storage
from os import environ
from api.v1.blueprints import app_views
from flask import Flask, make_response, jsonify, render_template
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
import secrets

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.debug = True
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.secret_key = secrets.token_hex(32)


@app.teardown_appcontext
def close_db(error):
    """close storage"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ 404 error
    ---
    responsees:
        404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': 'Not found'}), 404)

app.config['SWAGGER'] = {
        'title': 'Data_Storage_Engine API',
        'uiversion': 1
}
swagger = Swagger(app)

if __name__ == "__main__":
    """run application"""
    app.run(host='0.0.0.0', port='5001', threaded=True)
