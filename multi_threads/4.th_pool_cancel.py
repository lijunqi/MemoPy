import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed, CancelledError

def task_worker(n):
    print(f"[{time.strftime('%X')}]Task Start [{n}] in thread {threading.current_thread().ident}")
    for _ in range(2*n):
        time.sleep(1)
    print(f"[{time.strftime('%X')}]Task End {n}")
    return n

def canceller(fut_list):
    print(f"[{time.strftime('%X')}]Canceller running.")
    time.sleep(5)
    print(f"[{time.strftime('%X')}]Start to cancel.")
    """ Attempt to cancel the call.
    If the call is currently being executed or finished running and cannot be cancelled then the method will return False,
    otherwise the call will be cancelled and the method will return True.
    """
    for fut in fut_list:
        print(f"[{time.strftime('%X')}]do cancel: {fut.cancel()}")


def main():

    with ThreadPoolExecutor(max_workers=5) as executor:
        fut_list= []
        for i in range(5):
            fut_list.append(executor.submit(task_worker, i+2))

        cancel_th = threading.Thread(target=canceller, args=(fut_list,))
        cancel_th.start()

        fut_res = []
        for fut in as_completed(fut_list):
            try:
                fut.result()
#                fut_res.append(fut.result())
            except CancelledError:
                print('Future Cancel')
    
#        for data in fut_res:
#            print(f"[{time.strftime('%X')}]>>> data = {data}.")

        cancel_th.join()


if __name__ == '__main__':
    main()
    print('Done.')
