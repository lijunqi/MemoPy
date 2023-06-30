import asyncio
import time

# The asyncio.create_task() function to run coroutines concurrently
# as asyncio Tasks.
async def say_after(delay, what):
#    print(f"[{time.strftime('%X')}] {delay}, {what}")
    await asyncio.sleep(delay)
    print(f"[{time.strftime('%X')}]{what}")

async def main():
    # "Tasks" are used to schedule coroutines concurrently.
    # When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"[{time.strftime('%X')}]======  Begin sleep")
#    time.sleep(5)
    await asyncio.sleep(5)
    print(f"[{time.strftime('%X')}]======  After sleep")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task2
    print(f"[{time.strftime('%X')}]======  Here call await.")
    await task1

    print(f"[{time.strftime('%X')}]Finish")

asyncio.run(main())