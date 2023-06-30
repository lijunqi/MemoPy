import time
import asyncio
import concurrent.futures

def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    print(f"[{time.strftime('%X')}]Start to run blocking IO.")
    time.sleep(5)
    return 'blocking io done'
#    with open('/dev/urandom', 'rb') as f:
#        return f.read(100)

def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    print(f"{time.strftime('%X')}Start to run CPU bound.")
    return sum(i * i for i in range(10 ** 7))

async def main():
    loop = asyncio.get_running_loop()

    ## Options:

    # 1. Run in the default loop's executor:
    print(1)
    result = await loop.run_in_executor(None, blocking_io)
    print(f"[{time.strftime('%X')}]1. Default thread pool: {result}")

    # 2. Run in a custom thread pool:
    print(2)
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_io)
        print(f"[{time.strftime('%X')}]2. Custom thread pool: {result}")

    # 3. Run in a custom process pool:
#    with concurrent.futures.ProcessPoolExecutor() as pool:
#        result = await loop.run_in_executor(pool, cpu_bound)
#        print('3. Custom process pool: ', result)

print(f"[{time.strftime('%X')}]Start.")
asyncio.run(main())
print(f"[{time.strftime('%X')}]Done.")
