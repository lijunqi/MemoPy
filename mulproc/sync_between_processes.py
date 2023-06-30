import os
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print(f'[pid = {os.getpid()}] hello world {i}')
    finally:
        l.release()

def f2(i):
    print(f'[pid = {os.getpid()}] hello world {i}')

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
#        Process(target=f2, args=(num,)).start()
        Process(target=f, args=(lock, num)).start()