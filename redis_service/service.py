from socket import close
import threading
import time
import redis
from config import ServiceConfig
from redis_config import RedisConfig


class Service:
    """限流服务类，使用 Redis 实现固定窗口限流"""

    _pool = None

    @classmethod
    def _get_pool(cls):
        if cls._pool is None:
            cls._pool = redis.ConnectionPool(**RedisConfig.get_pool_kwargs())
        return cls._pool

    def __init__(self) -> None:
        self.redis = redis.Redis(connection_pool=self._get_pool())
        pass

    def get_user_level(self, user_id: str) -> str:
        return ServiceConfig.get_user_levels().get(user_id, "none")

    def service(self, user_id: str) -> None:
        level = self.get_user_level(user_id)
        max_calls = ServiceConfig.get_level_calls().get(level, 0)

        if max_calls == 0:
            print(f"[{user_id}] (等级: {level}) 无调用权限")
            return

        key = f"compid:{user_id}"

        try:
            count = self.redis.get(key)

            if count is None:
                self.redis.set(key, 1, ex=20)
                print(f"[{user_id}] 🔑 创建 Key: {key}, 初始值=1, 过期时间=20秒")
                count = 1
            else:
                count = int(count)

                if count >= max_calls:
                    ttl = self.redis.ttl(key)
                    print(
                        f"[{user_id}] (等级: {level}) 已达到上限 ({max_calls})，"
                        f"Key: {key}, 当前值={count}, 剩余TTL={ttl}秒"
                    )
                    return

                count = self.redis.incr(key)
                ttl = self.redis.ttl(key)
                print(f"[{user_id}] 🔑 Key: {key}, 自增后值={count}, 剩余TTL={ttl}秒")

            print(f"[{user_id}] (等级: {level}) 调用次数: {count}/{max_calls}")
            self._business()

        except redis.RedisError as e:
            print(f"[{user_id}] Redis 错误: {e}")

    def _business(self):
        print("  执行业务操作 -", time.strftime("%H:%M:%S"))

    def close(self):
        if Service._pool is not None:
            Service._pool.disconnect()
            Service._pool = None
            print("连接池已关闭")

    def __del__(self):
        self.close()


class MyThread(threading.Thread):
    def __init__(self, user_id: str, service: Service, interval: int = 1) -> None:
        super().__init__()
        self.user_id = user_id
        self.service = service
        self.interval = interval
        self._stop_event = threading.Event()
        pass

    def run(self) -> None:
        while not self._stop_event.is_set():
            self.service.service(self.user_id)
            time.sleep(self.interval)
        pass

    def stop(self):
        self._stop_event.set()
        pass
