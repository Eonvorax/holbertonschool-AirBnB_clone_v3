#!/usr/bin/python3
"""
This is the app module
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "http://0.0.0.0"}})


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown
    """
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors and return a JSON response.
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    api_host = getenv("HBNB_API_HOST", "0.0.0.0")
    api_port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=api_host, port=api_port, threaded=True)
