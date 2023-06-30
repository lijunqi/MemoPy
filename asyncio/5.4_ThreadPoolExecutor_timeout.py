import time
import threading
import concurrent.futures

def blocking_io(n):
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    thread_id = threading.current_thread().ident
    print(f"[{time.strftime('%X')}]Start to run blocking IO {n}. ThreadId: {thread_id}")
    cnt = 1
    x = 2
    for _ in range(x):
        print(f"[{time.strftime('%X')}][n={n}]Sleep {cnt}")
        time.sleep(5)
        cnt += 1
    return f'[Done]blocking io {n}'


def main():
    print(f"[{time.strftime('%X')}]start to wait")
    # 1. Run in the default loop's executor:
    print(f'Main thread id: {threading.current_thread().ident}')

    # 2. Run in a custom thread pool:
    n_threads = 3
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as tpe:
        fut_list = []
        for i in range(n_threads):
            fut_list.append(tpe.submit(blocking_io, i))
        
        for fut in fut_list:
            try:
                print(f"[{time.strftime('%X')}]ha")
                fut.result(timeout=3)
            except concurrent.futures.TimeoutError:
                # * Throw 3 TimeoutError exception because call fut.result 3 times
                print(f"[{time.strftime('%X')}]!!! Timeout !!!")

    print(f"[{time.strftime('%X')}]Done")


main()
