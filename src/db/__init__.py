"""Database pacakage."""

from redis_om import get_redis_connection

from src.config import settings

redis_conn = get_redis_connection(
    host=settings.redis_endpoint,
    port=settings.redis_port,
    password=settings.redis_password,
    decode_responses=True,
)
