""" Timestamp """
from datetime import datetime

now = datetime.now()
print("Local Now: ", now)
ts = now.timestamp()
print("Timestamp: ", ts, type(ts))

date = datetime.fromtimestamp(ts)
print("date(loc): ", date, type(date))

date = datetime.fromtimestamp(ts)
print("date(utc): ", date)
