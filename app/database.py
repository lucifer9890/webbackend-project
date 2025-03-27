from pymongo import MongoClient
from app.config import Config

client = MongoClient(Config.MONGO_URI)
db = client["flaskdb"]
