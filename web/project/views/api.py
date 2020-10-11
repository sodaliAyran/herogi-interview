from flask import Blueprint, jsonify, request
from project import dba

api_bp = Blueprint('api', __name__)

@api_bp.route('/get_values', methods=["GET"])
def get_values():
    results = dba.get_values()

    return jsonify(results)

@api_bp.route("/", methods=["GET"])
def api_check():
    return jsonify(hello="world")
