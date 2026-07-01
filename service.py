import threading
import time
import redis

# ==================== 配置 ====================
LEVEL_CALLS = {"none": 0, "low": 5, "medium": 10, "high": 20}

USER_LEVELS = {"A": "low", "B": "medium", "C": "high", "D": "none"}


# ==================== 服务类 ====================
class Service:
    def __init__(self) -> None:
        self.redis = redis.Redis(
            host="localhost", port=6379, db=0, decode_responses=True
        )

    def get_use_level(self, user_id: str) -> str:
        return USER_LEVELS.get(user_id, "none")

    def service(self, user_id: str) -> None:
        level = self.get_use_level(user_id)
        max_calls = LEVEL_CALLS.get(level, 0)

        if max_calls == 0:
            print(f"[{user_id}] (等级: {level}) 无调用权限")
            return

        key = f"compid:{user_id}"
        try:
            count = self.redis.get(key)
            if count is None:
                # 第一次，设置过期时间20秒，初始值1
                self.redis.set(key, 1, ex=20)
                # 打印 Key 创建信息
                print(f"[{user_id}] 🔑 创建 Key: {key}, 初始值=1, 过期时间=20秒")
                count = 1
            else:
                assert isinstance(count, str)
                count = int(count)
                if count >= max_calls:  # 达到上限
                    # 打印当前 Key 的状态（已达到上限）
                    ttl = self.redis.ttl(key)  # 查询剩余过期时间
                    print(
                        f"[{user_id}] (等级: {level}) 已达到上限 ({max_calls})，Key: {key}, 当前值={count}, 剩余TTL={ttl}秒"
                    )
                    return
                # 自增
                new_count = self.redis.incr(key)

                assert isinstance(new_count, int)
                count = int(new_count)
                # 打印自增后的 Key 状态
                ttl = self.redis.ttl(key)
                print(f"[{user_id}] 🔑 Key: {key}, 自增后值={count}, 剩余TTL={ttl}秒")

            print(f"[{user_id}] (等级: {level}) 调用次数: {count}/{max_calls}")
            self.business()
        except redis.RedisError as e:
            print(f"[{user_id}] Redis 错误: {e}")

    def business(self):
        print("  执行业务操作 -", time.strftime("%H:%M:%S"))

    def close(self):
        self.redis.close()
        print("连接已经关闭")

    def __del__(self):
        self.close()


# ==================== 线程类 ====================


class MyThread(threading.Thread):
    def __init__(self, user_id: str, service: Service, interval: int = 1):
        super().__init__()
        self.user_id = user_id
        self.service = service
        self.interval = interval
        self._stop_event = threading.Event()  # 用于控制线程停止

    def run(self) -> None:
        while not self._stop_event.is_set():
            self.service.service(self.user_id)
            time.sleep(self.interval)

    def stop(self):
        self._stop_event.set()


# ==================== 主程序 ====================
if __name__ == "__main__":
    svc = Service()
    threads = []

    for uid in ["A", "B", "C", "D"]:
        t = MyThread(uid, svc, interval=1)
        t.start()
        threads.append(t)

    time.sleep(25)

    for t in threads:
        t.stop()

    for t in threads:
        t.join()

    svc.close()
    print("结束")
