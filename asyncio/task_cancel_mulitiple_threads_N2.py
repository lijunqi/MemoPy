import time
import asyncio
import threading

class A():
    task = None
    task2 = None
    stop = False

    def __init__(self) -> None:
        pass
    
    @classmethod
    async def wait_for_cancel(cls):
        while not A.stop:
            await asyncio.sleep(1)
            print('not stop')
        print('start to cancel')
        A.task.cancel()
        print('finish to cancel')

    @classmethod
    async def slow_file(cls):
        print(f"[{time.strftime('%X')}][Start]slow file")
        await asyncio.sleep(10)
        print(f"[{time.strftime('%X')}][Finish]slow file")


    async def run(self):
        A.task = asyncio.create_task(A.slow_file())
        A.task2 = asyncio.create_task(A.wait_for_cancel())
        aw = asyncio.gather(A.task, A.task2)
        try:
            await asyncio.wait_for(aw, timeout=20)
        except asyncio.CancelledError:
            print(f"[{time.strftime('%X')}]Cancelled!")
        except Exception as exc:
            print(f"[{time.strftime('%X')}]Other exception: {str(exc)}")
        finally:
            print(f"[{time.strftime('%X')}]Do finally.")



def do_cancel():
    print(f"[{time.strftime('%X')}](Ready)do cancel")
    time.sleep(2)
    A.stop = True
#    A.cancel_me()
    print(f"[{time.strftime('%X')}](Done)do cancel")


async def main():

    task_a = A()

    th = threading.Thread(target=do_cancel)
    th.start()

    await task_a.run()

    th.join()

asyncio.run(main())
