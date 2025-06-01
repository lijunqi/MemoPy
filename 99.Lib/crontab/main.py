from crontab import CronTab
from cron_descriptor import get_description, ExpressionDescriptor, Options

import pytz
from datetime import datetime, timezone, timedelta


def _seconds_to_hh_mm_ss(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02}h {int(minutes):02}m {int(seconds):02}s"


def cal_cron(expr, tz_str):
    ct = CronTab(expr)
    user_local_now = datetime.now(pytz.timezone(tz_str))
    prev_delay_s = -1 * ct.previous(user_local_now, default_utc=False)
    prev_start = user_local_now + timedelta(seconds=prev_delay_s)
    next_delay_s = ct.next(user_local_now, default_utc=False)
    next_start = user_local_now + timedelta(seconds=next_delay_s)
    print(f"====== Timezone: {tz_str}")
    print(f"{expr}: {get_description(expr)}")
    print(f"\tUser  Now :  {user_local_now} --- {tz_str}")
    print(f"\tPrev time :  {_seconds_to_hh_mm_ss(prev_delay_s)} before ({int(prev_delay_s)}seconds)")
    print(f"\tPrev start:  {prev_start}")
    print(f"\tNext time :  {_seconds_to_hh_mm_ss(next_delay_s)} later ({int(next_delay_s)}seconds)")
    print(f"\tNext start:  {next_start}")
    print("next > prev: ", next_start > prev_start)
    print(type(next_start))
    print()


def invalid_cron(expr):
    try:
        ct = CronTab(expr)
        ct.next(datetime.now())
    except Exception as e:
        print(f"{expr}: {e}")

if __name__ == '__main__':
    utc_now = datetime.now(timezone.utc)
    loc_now = datetime.now()
    print(f"UTC Now:  {utc_now}")
    print(f"Loc Now:  {loc_now}")

    # At every 5th minute from 0 through 59.
    cal_cron('0/5 * * * * *', 'US/Eastern')

    # At 08:00 on every day-of-week from Monday through Friday.
    cal_cron('0 8 * * 1-5', 'Asia/Shanghai')
    cal_cron('0 8 * * 1-5', 'America/Chicago')
    cal_cron('0 8 * * 1-5', 'Europe/Warsaw')

    invalid_cron('a b c d e f g')

    print(str(ExpressionDescriptor("* 2 3 * *")))
