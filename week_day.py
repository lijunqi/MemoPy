from datetime import *
from enum import Enum

class Week(Enum):
    """ Enum for week """
    MON = 64
    TUE = 32
    WED = 16
    THU = 8
    FRI = 4
    SAT = 2
    SUN = 1

def is_active(day: datetime, week_mark: str) -> bool:
    return 1 << (6 - day.weekday()) & int(week_mark, 2) > 0


if __name__ == '__main__':
    mon = datetime(2025, 2, 10)
    tue = datetime(2025, 2, 11)
    wed = datetime(2025, 2, 12)
    thu = datetime(2025, 2, 13)
    fri = datetime(2025, 2, 14)
    sat = datetime(2025, 2, 15)
    sun = datetime(2025, 2, 16)

    days = [mon, tue, wed, thu, fri, sat, sun]

    if (mon.weekday() != 0 or tue.weekday() != 1 or wed.weekday() != 2 or thu.weekday() != 3 or fri.weekday() != 4 or sat.weekday() != 5 or sun.weekday() != 6):
        print('Weekday Error')
    else:
        mark = '1111100'
        print('Mark:', mark)
        for day in days:
            print(day, is_active(day, mark))

        mark = '1010100'
        print('Mark:', mark)
        for day in days:
            print(day, is_active(day, mark))
