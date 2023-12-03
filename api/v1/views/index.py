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
    """
    Retrieves the number of each object by type.
    """
    object_counts = {}
    for key in storage.all().keys():
        object_counts[key] = storage.count(key)
    return jsonify(object_counts)
