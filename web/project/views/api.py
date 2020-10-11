from flask import Blueprint, jsonify, request
from project import dba

api_bp = Blueprint('api', __name__)

@api_bp.route('/get_values', methods=["GET", "POST"])
def get_values():
    if request.json:
        sort = request.json.get("sort", None)
        results = dba.get_values(sort=sort)
    else:
        results = dba.get_values()

    return jsonify(results)

@api_bp.route("/", methods=["GET"])
def api_check():
    return jsonify(hello="world")
