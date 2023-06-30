import time
import asyncio
import threading

class A():

    def __init__(self) -> None:
        self.task = None
        self.task2 = None
        self.stop = False
    
    async def wait_for_cancel(self):
        while not self.stop:
            await asyncio.sleep(1)
            print('not stop')
        print('start to cancel')
        self.task.cancel()
        print('finish to cancel')

    async def slow_file(self):
        print(f"[{time.strftime('%X')}][Start]slow file")
        await asyncio.sleep(10)
        print(f"[{time.strftime('%X')}][Finish]slow file")


    async def run_monitor(self):
        self.task2 = asyncio.create_task(self.wait_for_cancel())
        await self.task2

    async def run(self):
        self.task = asyncio.create_task(self.slow_file())
        try:
            await asyncio.wait_for(self.task, timeout=5)
        except asyncio.CancelledError:
            print(f"[{time.strftime('%X')}]Cancelled!")
        except asyncio.TimeoutError:
            print(f"[{time.strftime('%X')}]Timeout!")
        except Exception as exc:
            print(f"[{time.strftime('%X')}]Other exception: {str(exc)}")
        finally:
            print(f"[{time.strftime('%X')}]Do finally.")
        print('quit')


def do_cancel(task_obj):
    print(f"[{time.strftime('%X')}](Ready)do cancel")
    time.sleep(20)
    task_obj.stop = True
    print(f"[{time.strftime('%X')}](Done)do cancel")


async def main():

    task_a = A()

    th = threading.Thread(target=do_cancel, args=(task_a,))
    th.start()

    await asyncio.gather(task_a.run(), task_a.run_monitor())

    th.join()

asyncio.run(main())
