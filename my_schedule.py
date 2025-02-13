import schedule
import time

def job_that_executes_once():
    # Do some work that only needs to happen once...
    print("I'm working...")
    return schedule.CancelJob

#schedule.every().day.at('08:31', 'Asia/Shanghai').do(job_that_executes_once)
schedule.every().minutes.do(job_that_executes_once)

while True:
    schedule.run_pending()
    print("I'm waiting...")
    time.sleep(1)