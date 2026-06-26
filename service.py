import threading
import time


class Service:
    def business(self):
        print("业务操作执行")


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.sc = Service()  # 创建Service 实例
        self._stop_event = threading.Event()  # 用于控制线程停止

    def run(self) -> None:
        return super().run()
