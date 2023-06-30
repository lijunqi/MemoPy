import time
import threading
import asyncio
from typing import Optional

from fastapi import FastAPI, Request, Body

app = FastAPI()


#@app.get("/")
#async def read_root():
#    print(f"[{time.strftime('%x')}]Get request.")
##    time.sleep(2)
#    await asyncio.sleep(2)
#    print(f"[{time.strftime('%x')}]Get request.")
#    return {"Hello": "World"}


#@app.get("/sync/{item_id}")
#def sync_read_item(item_id: int, payload: dict=Body()):
#    # * This is Mulitiple threads handler, time.sleep(n) will handle concurrently.
#    print('[Sync_Receive]thread id: ', threading.current_thread().ident, f'item_id: {item_id}')
#    print(type(payload), payload)
#    time.sleep(3)
##    time.sleep(int(item_id))
##    print(req.body())
#    return {"item_id": item_id}

@app.get("/ping/{delay}")
def async_read_item(delay: int):
    # * This is async handler, time.sleep(n) will block, not concurrently.
    print(f"[{time.strftime('%X')}](Async_Receive)thread id: ",
            threading.current_thread().ident, f'delay: {delay}')
    time.sleep(int(delay))
    return {"delay": delay}
