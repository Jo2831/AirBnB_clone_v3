#!/usr/bin/python3
"""Python file that routes the Flask API's"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def view_status():
    """An end point to retrive ok status as a response"""
    return jsonify({"status": "OK"})
