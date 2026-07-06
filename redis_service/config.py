import os
import yaml
from typing import Any, Dict


# ============================================================
# 基础配置加载器
# ============================================================
class BaseConfig:
    """通用配置加载器，支持 yaml + 环境变量覆盖"""

    _config: Dict[str, Any] = {}
    _loaded = False

    @classmethod
    def load(cls, config_path: str = "config.yaml"):
        if cls._loaded:
            return cls

        if not os.path.exists(config_path):
            raise FileExistsError(f"配置文件 {config_path} 不存在")

        with open(config_path, "r", encoding="utf-8") as f:
            cls._config = yaml.safe_load(f) or {}

        # 环境变量覆盖（例如 REDIS_HOST=xxx 会覆盖配置文件中的值）
        for section in cls._config:
            if isinstance(cls._config[section], dict):
                for key in list(cls._config[section].keys()):
                    env_key = f"{section.upper()}_{key.upper()}"
                    if os.getenv(env_key) is not None:
                        cls._config[section][key] = os.getenv(env_key)

        cls._loaded = True
        return cls

    @classmethod
    def get(cls, key: str, default=None):
        """获取配置项，支持点号分隔的多级 key，如 'redis.host'"""
        if not cls._loaded:
            cls.load()

        keys = key.split(".")
        vaule = cls._config

        for k in keys:
            if isinstance(vaule, dict) and k in vaule:
                vaule = vaule[k]
            else:
                return default

        return vaule


# ============================================================
# 业务配置（会员等级、用户映射）
# ============================================================
class ServiceConfig:
    """业务配置类（与基础设施配置分离）"""

    @staticmethod
    def get_level_calls() -> Dict[str, int]:
        """会员等级 -> 每20秒最大调用次数"""
        return {  #
            "none": 0,  #
            "low": 5,  #
            "medium": 10,  #
            "high": 20,  #
        }

    @staticmethod
    def get_user_levels() -> Dict[str, str]:
        """用户ID -> 会员等级映射"""
        return {  #
            "A": "low",  #
            "B": "medium",  #
            "C": "high",  #
            "D": "none",  #
        }


# ============================================================
# 初始化（程序启动时自动加载）
# ============================================================
BaseConfig.load()
