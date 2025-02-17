#!/usr/bin/python3
""" Index view for API """

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", methods=["GET"])
def get_status():
    """ get API status """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_stats():
    """
    Gets the number of objects for each type.
    """
    from models import storage
    from models.user import User
    return jsonify({
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    })
