from flask import Blueprint, jsonify
from project.models import User

api_bp = Blueprint('api', __name__)

@api_bp.route('/get_values', methods=["POST"])
def get_values():

    return jsonify(hello="world")

@api_bp.route("/", methods=["GET"])
def api_check():
    return jsonify(hello="world")
