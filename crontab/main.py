from crontab import CronTab
from datetime import datetime, timezone, timedelta


if __name__ == '__main__':
    # At every 5th minute from 0 through 59.
    entry = CronTab('0/5 * * * * *')
    now = datetime.now(timezone.utc)
    print(now, entry.next(default_utc=False))

    # At 08:00 on every day-of-week from Monday through Friday.
    entry = CronTab('0 8 * * 1-5')
    now = datetime.now(timezone.utc)
    delay_s = entry.next(default_utc=True)
    target_t = now + timedelta(seconds=delay_s)
    print("Now   : ", now)
    print("Delay : ", delay_s)
    print("Target: ", target_t)
