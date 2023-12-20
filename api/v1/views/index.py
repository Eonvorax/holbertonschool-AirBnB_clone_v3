#!/usr/bin/python3
"""
Routes module for api
"""


from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def status():
    """
    Returns the status of the server in JSON format
    """
    return jsonify({"status": "OK"})
