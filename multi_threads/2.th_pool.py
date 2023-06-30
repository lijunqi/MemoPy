import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
def task_worker(n):
    print(f"[{time.strftime('%X')}]Start [{n}] in thread {threading.current_thread().ident}")
    time.sleep(n)
    print(f"[{time.strftime('%X')}]End {n}")
    return n


with ThreadPoolExecutor(max_workers=2) as executor:
    tasks = []
    for i in range(3):
        tasks.append(executor.submit(task_worker, i+2))
        time.sleep(5)
    
    for task in as_completed(tasks):
        data = task.result()
        print(f"[{time.strftime('%X')}]>>> data = {data}")



print('Done.')
