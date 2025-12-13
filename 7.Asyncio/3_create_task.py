import asyncio
import time

# * The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
async def say_after(delay, what):
    print(f"[{time.strftime('%X')}]>>> [{what}] is started, wait for {delay}s")
    print(f"[{time.strftime('%X')}]\t\t[{what}] do something.")
    print(f"[{time.strftime('%X')}]\t\t[{what}] ready to await.")
    await asyncio.sleep(delay)
    #time.sleep(delay) # ! This would block the event loop, cause task2 start after task1 finish
    print(f"[{time.strftime('%X')}]<<< [{what}] is completed.")


async def main():
    # * "Tasks" are used to schedule coroutines concurrently.
    #   When a coroutine is wrapped into a Task with functions like asyncio.create_task()
    #   the coroutine is automatically scheduled to run soon
    print(f"[{time.strftime('%X')}]======  Create task1, task2")
    task1 = asyncio.create_task(say_after(1, 'Task 1'))
    task2 = asyncio.create_task(say_after(3, 'Task 2'))
    task3 = asyncio.create_task(say_after(5, 'Task 3'))
    task4 = asyncio.create_task(say_after(7, 'Task 4'))

    print(f"[{time.strftime('%X')}]======  Sync Sleep 1s")
    time.sleep(1)
    print(f"[{time.strftime('%X')}]Schedule coroutines are not executed until await.")
    time.sleep(1)
    sleep_sec = 5
    print(f"[{time.strftime('%X')}]Await async sleep {sleep_sec}s.")
    await asyncio.sleep(sleep_sec)
    print(f"[{time.strftime('%X')}]After async sleep {sleep_sec}s")

    # Wait until both tasks are completed (should take around 7 seconds.)
    print(f"[{time.strftime('%X')}]======  Await task2.")
    await task2
    print(f"[{time.strftime('%X')}]======  Await task2.")
    await task2
    print(f"[{time.strftime('%X')}]======  Await task2.")
    await task2
    print(f"[{time.strftime('%X')}]======  Await task1.")
    await task1
    print(f"[{time.strftime('%X')}]======  Await task1.")
    await task1
    print(f"[{time.strftime('%X')}]======  Await task1.")
    await task1

    await task3
    await task4

    print(f"[{time.strftime('%X')}]Finish")

asyncio.run(main())
