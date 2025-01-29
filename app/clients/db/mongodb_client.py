from pymongo import MongoClient
from app.config.app_config import settings

class MongoDBClient:
    def __init__(self, uri: str = settings.MONGODB_URI):
        self.client = MongoClient(uri)
        self.db = self.client.get_default_database()

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

    def close(self):
        self.client.close()