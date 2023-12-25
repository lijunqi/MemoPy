""" Use global variable """
time = 0

def insert_time(min):
    global  time # UnboundLocalError without this line
    time = time + min
    return  time

print(insert_time(2))
print(insert_time(10))