import time
import asyncio
import threading

async def slow_file():
    print(f"[{time.strftime('%X')}][Start]slow file")
    await asyncio.sleep(10)
    print(f"[{time.strftime('%X')}][Finish]slow file")

class A():
    def __init__(self) -> None:
        self.task = None
    
    def cancel_me(self):
        self.task.cancel()

    async def run(self):
        self.task = asyncio.create_task(slow_file())
        try:
            await self.task
#            await asyncio.wait_for(self.task, timeout=20)
        except asyncio.CancelledError:
            print(f"[{time.strftime('%X')}]Cancelled!")
        except Exception as exc:
            print(f"[{time.strftime('%X')}]Other exception: {str(exc)}")
        finally:
            print(f"[{time.strftime('%X')}]Do finally.")



def do_cancel(task_obj):
    print(f"[{time.strftime('%X')}](Ready)do cancel")
    time.sleep(2)
    task_obj.cancel_me()
    print(f"[{time.strftime('%X')}](Done)do cancel")


async def main():

    task_a = A()

    th = threading.Thread(target=do_cancel, args=(task_a,))
    th.start()

    await task_a.run()

    th.join()

asyncio.run(main())
