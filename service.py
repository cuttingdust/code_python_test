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
        while not self._stop_event.is_set():
            self.sc.business()
            time.sleep(1)
        return super().run()

    def stop(self):
        self._stop_event.set()


# 使用
if __name__ == "__main__":
    t = MyThread()
    t.start()

    # 5 秒后停止
    time.sleep(5)
    t.stop()
    t.join()
