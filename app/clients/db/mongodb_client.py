from pymongo import MongoClient
from app.core.config import settings
from typing import Any
from app.monitoring.logging import get_logger
from pymongo.collection import Collection
from pymongo.database import Database




logger = get_logger(__name__)

class MongoDBClient:
    def __init__(self, uri: str = settings.MONGODB_URI):
        try:
            self.client = MongoClient(
                uri,
                serverSelectionTimeoutMS=5000,  # 5 second timeout
                maxPoolSize=50,
                waitQueueTimeoutMS=1000
            )
            # Verify connection
            self.client.server_info()
            self.db: Database = self.client.get_default_database()
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {str(e)}")
            raise ConnectionError(f"Failed to connect to MongoDB: {str(e)}")

    def get_collection(self, collection_name: str) -> Collection:
        try:
            return self.db[collection_name]
        except Exception as e:
            logger.error(f"Failed to get collection {collection_name}: {str(e)}")
            raise RuntimeError(f"Failed to get collection {collection_name}: {str(e)}")

    def close(self):
        try:
            self.client.close()
        except Exception as e:
            logger.error(f"Failed to close MongoDB connection: {str(e)}")
            raise RuntimeError(f"Failed to close MongoDB connection: {str(e)}")
        
    def __enter__(self) -> 'MongoDBClient':
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()
        


