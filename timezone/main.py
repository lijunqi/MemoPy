from datetime import datetime, timedelta
import pytz
from pytz import timezone


FMT = '%Y-%m-%d %H:%M:%S %Z%z'

def list_all_tz():
    for tz in pytz.all_timezones:
        print(tz)
    print("Total:", len(pytz.all_timezones))


def list_all_common_tz():
    for tz in pytz.common_timezones:
        print(tz)
    print("Total:", len(pytz.common_timezones))


def convert_tz():
    ea = pytz.timezone('US/Eastern')
    time_str = datetime.now().astimezone(pytz.utc).strftime(FMT)
    print(time_str)


def set_tz():
    now = datetime.now()
    ea = pytz.timezone('US/Eastern')
    now_with_ea_tz = ea.localize(now)
    print(f"Now   : {now}")
    print(f"Now EA: {now_with_ea_tz}")


if __name__ == "__main__":
    eastern = timezone('US/Eastern')
    print(eastern.zone)

    #list_all_tz()
    list_all_common_tz()

    set_tz()
