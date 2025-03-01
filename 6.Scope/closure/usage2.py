time = 0

def study_time(time):
    def insert_time(min):
        nonlocal  time
        time = time + min
        return time

    return insert_time


f = study_time(time)
print(f(2))
print(time)
print(f(10))
print(time)

print("====================")

def f1():
    n=999
    def f2():
        print(n)
    return f2

r = f1()
r()