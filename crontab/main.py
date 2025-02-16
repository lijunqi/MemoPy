from crontab import CronTab

from cron_descriptor import get_description, ExpressionDescriptor

from datetime import datetime, timezone, timedelta


def cal_cron(expr):
    entry = CronTab(expr)
    now = datetime.now(timezone.utc)
    delay_s = entry.next(default_utc=True)
    target_t = now + timedelta(seconds=delay_s)
    print("====== ", get_description(expr))
    print("Now   : ", now)
    print("Delay : ", delay_s)
    print("Target: ", target_t)


if __name__ == '__main__':
    # At every 5th minute from 0 through 59.
    cal_cron('0/5 * * * * *')

    # At 08:00 on every day-of-week from Monday through Friday.
    cal_cron('0 8 * * 1-5')
