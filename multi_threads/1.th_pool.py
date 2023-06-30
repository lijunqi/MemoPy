import time
import threading
from concurrent.futures import ThreadPoolExecutor
def task_worker(n):
    print(f"[{time.strftime('%X')}]Start in thread {threading.current_thread().ident}")
    time.sleep(n)
    print(f"[{time.strftime('%X')}]End")
    return n


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(task_worker, 5)
b = executor.submit(task_worker, 3)

print(a.result())
print(b.result())

print('Done.')
