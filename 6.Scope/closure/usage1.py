""" Use global variable """
time = 0

def insert_time(min):
    global  time # UnboundLocalError without this line
    time = time + min
    return  time

print(insert_time(2))
print(insert_time(10))


# * Averager
def averager1():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add

a = averager1()
print("a(10) = ", a(10)) # 10.0
print("a(20) = ", a(20)) # 15.0

def averager2():
    total = 0
    count = 0
    def add(number):
        nonlocal total, count
        total += number
        count += 1
        return total / count
    return add

a = averager2()
print("a(10) = ", a(10)) # 10.0
print("a(20) = ", a(20)) # 15.0
