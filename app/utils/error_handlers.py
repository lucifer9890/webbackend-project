from flask import jsonify

# 400 - Bad Request
def handle_bad_request(message="Bad Request"):
    return jsonify({
        "error": "Bad Request",
        "message": message
    }), 400

# 401 - Unauthorized
def handle_unauthorized(message="Unauthorized"):
    return jsonify({
        "error": "Unauthorized",
        "message": message
    }), 401

# 404 - Not Found
def handle_not_found(message="Not Found"):
    return jsonify({
        "error": "Not Found",
        "message": message
    }), 404

# 500 - Internal Server Error
def handle_internal_error(message="Internal Server Error"):
    return jsonify({
        "error": "Internal Server Error",
        "message": message
    }), 500

# Fallback error handler for unexpected errors
def handle_unexpected_error(error):
    return jsonify({
        "error": "Unexpected Error",
        "message": str(error)
    }), 500
