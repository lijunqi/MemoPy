import asyncio, time

async def t1(name, number):
    print(f"[{time.strftime('%X')}] Run {name}")
    await asyncio.sleep(number)
    print(f"[{time.strftime('%X')}] Done {name}")
    await asyncio.gather(
        t("task_3", 3),
        t("task_4", 4),
    )
    print(f"[{time.strftime('%X')}] Exit {name}")

async def t2(name, number):
    print(f"[{time.strftime('%X')}] Run {name}")
    await asyncio.sleep(number)
    print(f"[{time.strftime('%X')}] Done {name}")
    await asyncio.gather(
        t("task_5", 5),
        t("task_6", 6),
    )
    print(f"[{time.strftime('%X')}] Exit {name}")

async def t(name, number):
    print(f"[{time.strftime('%X')}] Run {name}")
    await asyncio.sleep(number)
    print(f"[{time.strftime('%X')}] Done {name}")


async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        t1("taks_1", 1),
        t2("taks_2", 2),
    )

    print('Done')

asyncio.run(main())

# Expected output:
#
#     Task A: Compute factorial(2)...
#     Task B: Compute factorial(2)...
#     Task C: Compute factorial(2)...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3)...
#     Task C: Compute factorial(3)...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4)...
#     Task C: factorial(4) = 24