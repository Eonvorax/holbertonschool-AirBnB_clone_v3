#!/usr/bin/python3
"""
Routes module for api
"""


from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """
    Returns the status of the server in JSON format
    """
    return jsonify({"status": "OK"})


@app_views.route("/api/v1/stats", strict_slashes=False)
def get_stats():
    """
    Retrieves the count of each class instance by class
    """
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }

    return jsonify(stats)
