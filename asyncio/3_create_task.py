import asyncio
import time

# The asyncio.create_task() function to run coroutines concurrently
# as asyncio Tasks.
async def say_after(delay, what):
    print(f"[{time.strftime('%X')}]Start [{what}], wait for {delay}s")
    await asyncio.sleep(delay)
    #time.sleep(delay) # ! This would block the event loop, cause task2 start after task1 finish
    print(f"[{time.strftime('%X')}]End [{what}]")

async def main():
    # "Tasks" are used to schedule coroutines concurrently.
    # When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon
    task1 = asyncio.create_task(
        say_after(3, 'Task 1'))

    task2 = asyncio.create_task(
        say_after(7, 'Task 2'))

    print(f"[{time.strftime('%X')}]======  Begin sleep")
    #time.sleep(5)
    await asyncio.sleep(5)
    print(f"[{time.strftime('%X')}]======  After sleep")

    # Wait until both tasks are completed
    # (should take around 7 seconds.)
    await task2
    await task2
    await task2
    print(f"[{time.strftime('%X')}]======  Here call await.")
    await task1
    await task1
    await task1

    print(f"[{time.strftime('%X')}]Finish")

asyncio.run(main())