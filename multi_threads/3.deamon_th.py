import time
import threading

'''
daemon线程:
当一个线程设置为daemon线程时, 主线程结束时, 不会因为daemon线程还没有结束运行而阻塞.
也就是主线程不管先daemon线程. 类比可以想像一下运行程序后启动一个主线程,然后又一个后台线程也启动.
如果这个程序要退出了, 却因为后台程序还在运行而无法退出, 这就不合适了.

非daemon线程:
当一个线程设置为非daemon线程时, 主线程结束时, 会检查所有非daemon的子线程是否结束.
如果还未结束, 则主线程等待非daemon结束后再退出.
'''

def func_daemon():
    print("Start daemon")
    time.sleep(5)
    print("End daemon")

def func_non_daemon():
    print("Start non-daemon")
    time.sleep(3)
    print("End non-daemon")

d = threading.Thread(target=func_daemon, daemon=True)
n = threading.Thread(target=func_non_daemon, daemon=False)

d.start()
n.start()

print('Done.')
