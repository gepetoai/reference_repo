from app.core.config import settings
import redis
from app.monitoring.logging import get_logger

logger = get_logger(__name__)

class RedisClient:
    def __init__(
        self,
        host: str = 'localhost',
        port: int = 6379,
        db: int = 0,
        password: str | None = None,
        ssl: bool = False,
        socket_timeout: float = 2.0
    ):
        try:
            self.client = redis.Redis(
                host=host,
                port=port,
                db=db,
                password=password,
                ssl=ssl,
                socket_timeout=socket_timeout,
                decode_responses=True  # Auto-decode to str
            )
            # Verify connection
            self.client.ping()
        except redis.ConnectionError as e:
            raise ConnectionError(f"Failed to connect to Redis: {str(e)}")


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

