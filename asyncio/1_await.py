import asyncio

async def main():
    print('hello')
    # sleep() always suspends the current task, allowing other tasks to run.
    await asyncio.sleep(2)
    print('world')

# This function always creates a new event loop and closes it at the end.
# It should be used as a main entry point for asyncio programs,
# and should ideally only be called once.
asyncio.run(main())