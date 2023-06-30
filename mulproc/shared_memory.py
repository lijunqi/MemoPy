from multiprocessing import Process, Value, Array

# Array: Return a ctypes array allocated from shared memory.

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    print(f'Init num is {num.value}')
    print(f'Init arr is {arr[:]}')
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(f'After num is {num.value}')
    print(f'After arr is {arr[:]}')