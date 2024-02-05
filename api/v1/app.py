#!/usr/bin/python3
""" start your API! """

import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)

app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
app_port = int(os.getenv('HBNB_API_PORT', 5000))
CORS(app, resources={'/*': {'origins': app_host}})


@app.teardown_appcontext
def teardown_flask(exception):
    """ Tear down the app context """
    storage.close()


@app.errorhandler(404)
def not_found_404(error):
    """ Handles error code. """
    return jsonify(error='Not found'), 404


@app.errorhandler(404)
def error_404(error):
    '''Handles the 404 HTTP error code.'''
    return jsonify(error='Not found'), 404


if __name__ == "__main__":
    """ Runs flask App """
    app.run(host=app_host, port=app_port, threaded=True)
