import time
import threading
import asyncio
import concurrent.futures

def blocking_io(n):
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    thread_id = threading.current_thread().ident
    print(f"[{time.strftime('%X')}]Start to run blocking IO {n}. ThreadId: {thread_id}")
    cnt = 1
    x = 3
    for _ in range(x):
        print(f'[Th={thread_id}]Sleep {cnt}')
        time.sleep(5)
        cnt += 1
    return f'[Done]blocking io {n}'


async def submain():
    loop = asyncio.get_running_loop()

    ## Options:

    # 1. Run in the default loop's executor:
    print(f'Submain thread id: {threading.current_thread().ident}')

    # 2. Run in a custom thread pool:
    print(2)
    n_threads = 5
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as pool:
        tasks = []
        for i in range(n_threads):
            tasks.append(loop.run_in_executor(pool, blocking_io, i))

#        for t in tasks:
#            t.cancel()
#            try:
#                await t
#            except asyncio.CancelledError:
#                print("cancel_me is cancelled now")

        results = await asyncio.gather(*tasks)
#        print(f"results type is {type(results)}")
#        print(f"[{time.strftime('%X')}]Result: {results}")

async def main():
    print(f'Main thread id: {threading.current_thread().ident}')
    main_task = asyncio.create_task(submain())
    
    print(f"[{time.strftime('%X')}]start to wait")
    await asyncio.sleep(1)
    print(f"[{time.strftime('%X')}]wait done")

#    print('call cancel')
#    main_task.cancel()
#    print('call cancel done')
#
#    try:
#        await main_task
#    except asyncio.CancelledError:
#        print("main(): cancel_me is cancelled now")


print(f"[{time.strftime('%X')}]Start.")
asyncio.run(main())
print(f"[{time.strftime('%X')}]Done.")
