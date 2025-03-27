from werkzeug.security import generate_password_hash, check_password_hash
from app.database import db

class User:
    @staticmethod
    def create_user(username, password):
        hashed_password = generate_password_hash(password)
        db.users.insert_one({"username": username, "password": hashed_password})

    @staticmethod
    def find_user(username):
        return db.users.find_one({"username": username})

    @staticmethod
    def verify_password(stored_password, provided_password):
        return check_password_hash(stored_password, provided_password)
