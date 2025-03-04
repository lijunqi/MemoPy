from crontab import CronTab
from cron_descriptor import get_description, ExpressionDescriptor, Options

import pytz
from datetime import datetime, timezone, timedelta


def cal_cron(expr, tz_str):
    ct = CronTab(expr)
    utc_now = datetime.now(timezone.utc)
    loc_now = datetime.now()
    now = datetime.now(pytz.timezone(tz_str))
    delay_s = ct.next(now, default_utc=True)
    target_t = now + timedelta(seconds=delay_s)
    print(f"====== ({expr}): {get_description(expr)}")
    print(f"UTC Now:  {utc_now}")
    print(f"Loc Now:  {loc_now}")
    print(f"Now    :  {now} --- {tz_str}")
    print(f"Delay(s):  {delay_s}")
    print(f"Delay(m):  {delay_s/60.0}")
    print(f"Target:  {target_t}")


if __name__ == '__main__':
    tz = 'US/Eastern'
    # At every 5th minute from 0 through 59.
    cal_cron('0/5 * * * * *', tz)

    # At 08:00 on every day-of-week from Monday through Friday.
    cal_cron('0 8 * * 1-5', tz)

    print(str(ExpressionDescriptor("* 2 3 * *")))
