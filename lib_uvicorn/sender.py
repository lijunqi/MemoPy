import time
import asyncio
import aiohttp

URL = "http://127.0.0.1:5000"


async def send_req(s, n):
    payload = {'a': n}
    async with aiohttp.ClientSession() as sess:
        print(f"[{time.strftime('%X')}]Send ", n)
        resp = await sess.get(f'{URL}/ping/{n}', json=payload)
        res = await resp.text()
        print(f"[{time.strftime('%X')}]Response ", n, res)


async def main():
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(send_req('', i+1)))
    
    await asyncio.gather(*tasks)

asyncio.run(main())
