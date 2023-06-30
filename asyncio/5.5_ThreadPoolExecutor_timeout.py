import concurrent.futures
import time
import datetime

"""
However, your program itself will keep on running until all running tasks have been completed.
This is because currently executing tasks (in your case, probably all your submitted tasks,
as your pool size equals the number of tasks), are not actually "killed".

The TimeoutError is raised, so that you can choose not to wait until the task is finished (and do something else instead),
but the task will keep on running until completed.
And python will not exit as long as there are unfinished tasks in the threads/subprocesses of your Executor.

As far as I know, it is not possible to just "stop" currently executing Futures,
you can only "cancel" scheduled tasks that have yet to be started.
In your case, there won't be any, but imagine that you have pool of 5 threads/processes,
and you want to process 100 items. At some point, there might be 20 completed tasks, 5 running tasks, and 75 tasks scheduled.
In this case, you would be able to cancel those 76 scheduled tasks, but the 4 that are running will continue until completed,
whether you wait for the result or not.
"""

max_numbers = [10000000, 10000000, 10000000, 10000000, 10000000]

class Task:
    def __init__(self, max_number):
        self.max_number = max_number
        self.interrupt_requested = False

    def __call__(self):
        print("Started:", datetime.datetime.now(), self.max_number)
        last_number = 0
        for i in range(1, self.max_number + 1):
            if self.interrupt_requested:
                print("Interrupted at", i)
                break
            last_number = i * i
        print("Reached the end")
        return last_number

    def interrupt(self):
        self.interrupt_requested = True

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(max_numbers)) as executor:
        tasks = [Task(num) for num in max_numbers]
        for task, future in [(i, executor.submit(i)) for i in tasks]:
            try:
                print(future.result(timeout=1))
            except concurrent.futures.TimeoutError:
                print("this took too long...")
                task.interrupt()


if __name__ == '__main__':
    main()