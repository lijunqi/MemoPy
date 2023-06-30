
import time
import asyncio

async def hello():
    print('Hello World:%s' % time.time())
    await asyncio.sleep(1)   
    print('Hello wow World:%s' % time.time())

def run():
    tasks = []
    for i in range(5):
        tasks.append(hello())
    loop.run_until_complete(asyncio.wait(tasks))

loop = asyncio.get_event_loop()
if __name__ =='__main__':
    run()
