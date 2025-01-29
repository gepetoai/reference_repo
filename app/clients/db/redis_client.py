from app.core.config import settings
import redis
from app.monitoring.logging import get_logger

logger = get_logger(__name__)

class RedisClient:
    def __init__(self, db: int = 0):
        self.client = redis.Redis(host=settings.REDIS_ENDPOINT, port=settings.REDIS_PORT, db=db)


    def set(self, key: str, value: str, ex: int | None = None) -> bool:
        """Set key to value with optional expiration in seconds."""
        try:
            return self.client.set(key, value, ex=ex)
        except redis.RedisError as e:
            logger.error(f"Failed to set key {key}: {str(e)}")
            raise RuntimeError(f"Failed to set key {key}: {str(e)}")


    def get(self, key: str) -> str | None:
        """Get value for key."""
        try:
            return self.client.get(key)
        except redis.RedisError as e:
            logger.error(f"Failed to get key {key}: {str(e)}")
            raise RuntimeError(f"Failed to get key {key}: {str(e)}")


    def delete(self, key: str) -> int:
        """Delete key, returns number of keys deleted."""
        try:
            return self.client.delete(key)
        except redis.RedisError as e:
            logger.error(f"Failed to delete key {key}: {str(e)}")
            raise RuntimeError(f"Failed to delete key {key}: {str(e)}")
