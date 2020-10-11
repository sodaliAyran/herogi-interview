from flask import Blueprint, jsonify, request
from project import dba

api_bp = Blueprint('api', __name__)

@api_bp.route('/get_values', methods=["GET"])
def get_values():
    # Had to do this because Javascript can't seem to sort floats
    results = sorted(dba.get_values(), key=lambda k: k["average_pace"])

    return jsonify(result=results)

@api_bp.route("/", methods=["GET"])
def api_check():
    return jsonify(hello="world")
