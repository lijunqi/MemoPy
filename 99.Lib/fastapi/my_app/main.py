import time
import threading
from typing import Annotated, Optional, Union, Dict, Any

from fastapi import FastAPI, Depends, Query, Path, Request, Body
from my_app.model import MyItem
from my_app.helper import other_server

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
def ping(delay: int):
    # * This is async handler, time.sleep(n) will block, not concurrently.
    print(f"[{time.strftime('%X')}](Async_Receive)thread id: ",
            threading.current_thread().ident, f'delay: {delay}')
    time.sleep(int(delay))
    return {"delay": delay}


# * Dependency injection
"""
虽然，在路径操作函数的参数中使用 Depends 的方式与 Body、Query 相同，但 Depends 的工作方式略有不同。

这里只能传给 Depends 一个参数。

且该参数必须是可调用对象，比如函数。

该函数接收的参数和路径操作函数的参数一样
"""
def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    print(f">>> common_parameters: q = {q}, skip = {skip}, limit = {limit}")
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


# ~ 从路径参数中获得uid
def check_admin(uid: int=Path()):
    print("====> uid: ", uid)
    if uid == 1:
        return {"is_admin": True}
    else:
        print(f"uid = {uid}")
        return {"is_admin": False}


# * 路径参数(用Path校验,元数据):
@app.get("/users/{uid}")
def read_users(uid: int, commons: Annotated[dict, Depends(check_admin)]):
    print("req: uid: ", uid)
    if commons['is_admin']:
        print("It is admin.")
    else:
        print("It is NOT admin.")
    return commons

@app.get("/items/{item_id}")
def read_item_by_id(
    item_id: int = Path(
        title="The ID of the item to get",
        description="A ID >= 1",
        ge=1
    ),
    q: str | None = Query(default=None, alias="item-query"),
):
    results: Dict[str, Any] = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# * 查询参数(用Query校验,元数据):
# * 例如: http://127.0.0.1:8000/elements/?skip=0&limit=10
# * 查询字符串是键值对的集合，这些键值对位于 URL 的 ? 之后，以 & 分隔
# * q 是可选的，但只要提供了该参数，则该参数值的字符长度为[3,10]之间
@app.get("/elements/")
def read_elements(
    q: str=Query(default="fixQ", min_length=3, max_length=10),
    skip: int=0,
    limit: int=10
    ):
    return {"q": q, "skip": skip, "limit": limit}


@app.post("/my_item/")
def create_item(item: MyItem):
    print(">>> Create item: ", item)
    print("item name: ", item.name)
    return item
