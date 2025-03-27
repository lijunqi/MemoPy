""" Convert str to datetime and vice versa """
from datetime import datetime

# ~ str to datetime ~
print("====== str to datetime ======")
iso_8601_str = '2011-11-04T00:05:23+04:00'
print("ISO8601: ", repr(datetime.fromisoformat(iso_8601_str)))
print("Custom: ", datetime.strptime(iso_8601_str, '%Y-%m-%dT%H:%M:%S%z'))

# ~ datetime to str ~
print("====== datetime to str ======")
dt = datetime.now()
print("Now: ", dt)
print("ISO8601: ", dt.isoformat())
print("Custom: ", dt.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
