import time

def foo():
    a = u'\u2502'
    for i in range(5):
        print("========= Hello")
        print("这是", i)
        print(a)
        time.sleep(1)

if __name__ == "__main__":
    foo()
