from typing import Any, Dict
from config import BaseConfig


class RedisConfig:
    """
    Redis 连接配置类
    职责：提供 Redis 连接池和单客户端所需的参数字典
    """

    @staticmethod
    def get_pool_kwargs() -> Dict[str, Any]:
        """返回创建 ConnectionPool 所需的参数字典"""
        return {  #
            "host": BaseConfig.get("redis.host", "localhost"),  #
            "port": BaseConfig.get("redis.port", 6379),  #
            "db": BaseConfig.get("redis.db", 0),  #
            "decode_responses": BaseConfig.get("redis.decode_responses", True),  #
            "max_connections": BaseConfig.get("redis.max_connections", 10),  #
            # "max_idle_time_seconds": BaseConfig.get("redis.max_idle_time_seconds"),  #
            "health_check_interval": BaseConfig.get(
                "redis.health_check_interval", 30
            ),  #
            "socket_timeout": BaseConfig.get("redis.socket_timeout", 5),  #
            "socket_connect_timeout": BaseConfig.get(
                "redis.socket_connect_timeout", 2
            ),  #
        }

    @staticmethod
    def get_client_kwargs() -> Dict[str, Any]:
        """返回创建单 Redis 客户端所需的参数字典（非连接池场景）"""
        return {  #
            "host": BaseConfig.get("redis.host", "localhost"),  #
            "port": BaseConfig.get("redis.port", 6379),  #
            "db": BaseConfig.get("redis.db", 0),  #
            "decode_responses": BaseConfig.get("redis.decode_responses", True),  #
            "socket_timeout": BaseConfig.get("redis.socket_timeout", 5),  #
            "socket_connect_timeout": BaseConfig.get(
                "redis.socket_connect_timeout", 2
            ),  #
        }

    @staticmethod
    def get_connection_url() -> str:
        """返回 Redis 连接 URL（适用于需要 URL 的场景）"""
        host = BaseConfig.get("redis.host", "localhost")
        port = BaseConfig.get("redis.port", 6379)
        db = BaseConfig.get("redis.db", 0)
        return f"redis://{host}:{port}/{db}"
