from flask import Blueprint, abort, jsonify

error_bp = Blueprint('error', __name__)

@error_bp.app_errorhandler(404)
def handle_four_oh_four_request(error):
    payload = {"message": "this endpoint does not exist."}
    return jsonify(payload), 404

@error_bp.app_errorhandler(400)
def handle_bad_request(error):
    payload = {"message": "request doesn't have the valid parameters."}
    return mjsonify(payload), 400

@error_bp.app_errorhandler(405)
def handle_method_not_allowed(error):
    payload = {"message": "this method is not allowed at this endpoint."}
    return jsonify(payload), 405


@error_bp.app_errorhandler(500)
def handle_internal(error):
    payload = {"message": "unexpected error, please try again later"}
    return jsonify(payload), 500
