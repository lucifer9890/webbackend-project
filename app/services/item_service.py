from app.models.item import Item

def create_item(name, description, username):
    return Item.create_item(name, description, username)

def get_all_items():
    return Item.get_all_items()

def update_item(item_id, name, description):
    return Item.update_item(item_id, name, description)

def delete_item(item_id):
    return Item.delete_item(item_id)