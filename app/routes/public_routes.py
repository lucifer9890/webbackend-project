from flask import Blueprint, jsonify

public_bp = Blueprint("public", __name__)

from app.services.item_service import get_all_items

# List all the items from database
@public_bp.route('/items', methods=['GET'])
def list_items():
    items = get_all_items()
    return jsonify({"items": items}), 200