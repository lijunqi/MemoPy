import time
import asyncio
import threading
import concurrent.futures

def blocking_io(n):
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    try:
        thread_id = threading.current_thread().ident
        print(f"[{time.strftime('%X')}]Start to run BlockingIO {n}. ThreadId: {thread_id}")
        cnt = 1
        x = n
        for _ in range(x):
            print(f"[{time.strftime('%X')}][n={n}]Sleep {cnt}")
            time.sleep(5)
            cnt += 1
        print(f"[{time.strftime('%X')}]BlockingIO done. n={n}.")
    finally:
        print(f"[{time.strftime('%X')}]Finally BlockingIO quit. n={n}.")
    return f'[Done]Blocking IO {n}'


async def main():
    print(f"[{time.strftime('%X')}]Start")
    # 1. Run in the default loop's executor:
    print(f'Main thread id: {threading.current_thread().ident}')

    # 2. Run in a custom thread pool:
    n_threads = 4
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as tpe:
        futures = []
        for i in range(n_threads):
            futures.append(tpe.submit(blocking_io, i))
        output_list = []
        print(f"[{time.strftime('%X')}]================")
        try:
            for fut in concurrent.futures.as_completed(futures, timeout=3):
                try:
                    print(f"[{time.strftime('%X')}]waiting for result")
                    output = fut.result()
                    print(f"[{time.strftime('%X')}]result output: {output}")
                except Exception as exc:
                    print('!!!!!>>>>')
        except concurrent.futures.TimeoutError:
            # * Only throw one TimeoutError exception
            print(f"[{time.strftime('%X')}]Timeout!!!!!!")
            # * Waiting for all future done
            while True:
                if all(fut.done() for fut in futures):
                    print(f"[{time.strftime('%X')}]All fut done.")
                    break
                print(f"[{time.strftime('%X')}]Waiting for fut done.")
                time.sleep(0.5)
        print(f"[{time.strftime('%X')}]Final Output: {output_list}")

    print(f"[{time.strftime('%X')}]Done")


asyncio.run(main())
