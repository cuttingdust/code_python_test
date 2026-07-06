import time
from service import Service, MyThread


def main():
    print("=" * 50)
    print("🚀 限流服务启动")
    print("=" * 50)

    svc = Service()
    threads = []

    for uid in ["A", "B", "C", "D"]:
        t = MyThread(uid, svc, interval=1)
        t.start()
        threads.append(t)

    print("运行中... (Ctrl+C 可提前终止)\n")

    try:
        time.sleep(25)
    except KeyboardInterrupt:
        print("\n收到中断信号，正在停止...")

    print("正在停止线程...")
    for t in threads:
        t.stop()

    for t in threads:
        t.join()

    svc.close()
    print("✅ 程序结束")


if __name__ == "__main__":
    main()
