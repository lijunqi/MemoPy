import time
import asyncio

async def eternity():
    # Sleep for one hour
    try:
        print(f"[{time.strftime('%X')}]start")
        await asyncio.sleep(5)
        print(f"[{time.strftime('%X')}]yay!")
    finally:
        print(f"[{time.strftime('%X')}]Finally Eternity.")
        #await asyncio.sleep(2)
        print(f"[{time.strftime('%X')}]Quit Eternity.")

async def main():
    # Wait for at most 1 second
    try:
        print(f"[{time.strftime('%X')}]Go!")
        task = asyncio.create_task(eternity())
        await asyncio.sleep(1)
        await asyncio.wait_for(task, timeout=3.0)
    except asyncio.TimeoutError:
        print(f"[{time.strftime('%X')}]timeout!")
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print('cancel!')

asyncio.run(main())

# Expected output:
#
#     timeout!
