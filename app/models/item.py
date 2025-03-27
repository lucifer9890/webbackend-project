from app.database import db
from bson import ObjectId 


class Item:
    @staticmethod
    def create_item(name, description, created_by):
        db.items.insert_one({
            "name": name,
            "description": description,
            "created_by": created_by
        })

    @staticmethod
    def get_all_items():
        return list(db.items.find({}, {"_id": 0}))

    @staticmethod
    def update_item(item_id, name, description):
        db.items.update_one(
            {"_id": ObjectId(item_id)},  # Use ObjectId
            {"$set": {"name": name, "description": description}}
        )

    @staticmethod
    def delete_item(item_id):
        db.items.delete_one({"_id": ObjectId(item_id)})  # Use ObjectId