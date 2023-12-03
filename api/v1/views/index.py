#!/usr/bin/python3

"""

solution for task 3(index.py):

"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage

@app_views.route("/status", strict_slashes=False, methods=["GET"])


def status():

    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def get_stats():
 
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)
