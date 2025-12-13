import time
import threading
import concurrent.futures

def blocking_io(n):
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    thread_id = threading.current_thread().ident
    print(f"[{time.strftime('%X')}]Start to run blocking IO {n}. ThreadId: {thread_id}")
    cnt = 1
    x = n
    for _ in range(x):
        print(f"[{time.strftime('%X')}][n={n}]Sleep {cnt}")
        time.sleep(5)
        cnt += 1
    return f'[Done]blocking io {n}'


def main():
    print(f"[{time.strftime('%X')}]Start")
    # 1. Run in the default loop's executor:
    print(f'Main thread id: {threading.current_thread().ident}')

    # 2. Run in a custom thread pool:
    n_threads = 3
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as tpe:
        futures = []
        for i in range(n_threads):
            futures.append(tpe.submit(blocking_io, i))
        output_list = []
        print(f"[{time.strftime('%X')}]================")
        try:
            for fut in concurrent.futures.as_completed(futures, timeout=3):
                print(f"[{time.strftime('%X')}]ha")
                try:
                    output = fut.result()
                    print(f"[{time.strftime('%X')}]output: {output}")
                except Exception as exc:
                    print('!!!!!>>>>')
        except concurrent.futures.TimeoutError:
            # * Only throw one TimeoutError exception
            print(f"[{time.strftime('%X')}]Timeout!!!!!!")
        print('Output: ', output_list)

    print(f"[{time.strftime('%X')}]Done")


main()
