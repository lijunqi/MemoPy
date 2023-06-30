import asyncio

class MyData():
    def __init__(self) -> None:
        self.data = 0


async def do_something_else():
    await asyncio.sleep(0.00001)


'''
预期是 100, 实际是 1.
因为协程 1 读到的 b 为 0, 遇到 await 切换到 f(),
再切回到协程 2, 读到的 b 为 0, 遇到 await 切换到 f(),
再切回到协程 3, 读到的 b 为 0, 当第 100 个协程切回到 f(),
最后切回协程 99, 此时 b+1 得到 1, 再切回协程 98, 此时 b+1 得到 1, 最终 a[0]=1
'''
async def add(user_dict):
    b = user_dict['number'].data
    await do_something_else()
    b += 1
    user_dict['number'].data  = b
    print('data = ', user_dict['number'].data)


async def lock_add(user_dict, lock, i):
    async with lock:
        print(f'This is {i} start.')
        b = user_dict['number'].data
        await f()
        b += 1
        user_dict['number'].data  = b
        print('data = ', user_dict['number'].data)
        print(f'This is {i} end.')


async def main():
    my_data = MyData()
    user_dict = {
        'number': my_data
    }
    lock = asyncio.Lock()
    coros = [lock_add(user_dict, lock, i) for i in range(10)]
#    coros = [add(user_dict) for _ in range(10)]
    await asyncio.gather(*coros)

    print("Done. ", user_dict['number'].data)


asyncio.run(main())
