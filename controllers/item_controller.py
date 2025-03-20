from flask import Blueprint, request, jsonify
from services.item_service import ItemService
from schemas.item_schema import ItemSchema

item_bp = Blueprint("item", __name__)
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

@item_bp.route("/", methods=["GET"])
def get_items():
    items = ItemService.get_all_items()
    return jsonify(items_schema.dump(items))

@item_bp.route("/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = ItemService.get_item_by_id(item_id)
    if not item:
        return jsonify({"message": "Item not found"}), 404
    return jsonify(item_schema.dump(item))

@item_bp.route("/", methods=["POST"])
def create_item():
    data = request.get_json()
    item = ItemService.create_item(data)
    return jsonify(item_schema.dump(item)), 201

@item_bp.route("/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    item = ItemService.update_item(item_id, data)
    if not item:
        return jsonify({"message": "Item not found"}), 404
    return jsonify(item_schema.dump(item))

@item_bp.route("/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = ItemService.delete_item(item_id)
    if not item:
        return jsonify({"message": "Item not found"}), 404
    return jsonify({"message": "Item deleted successfully"})