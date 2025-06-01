import time
from pytest import mark

# ! require: pytest-xdist
# ! pytest -s -v -nauto

@mark.slow
def test_slow_1():
    print(f"[{time.strftime('%X')}]slow 1 start")
    time.sleep(3)
    print(f"[{time.strftime('%X')}]slow 1 complete")

@mark.slow
def test_slow_2():
    print(f"[{time.strftime('%X')}]slow 2 start")
    time.sleep(3)
    print(f"[{time.strftime('%X')}]slow 2 complete")

@mark.slow
def test_slow_3():
    t = 3
    print(f"[{time.strftime('%X')}]slow 3 start")
    time.sleep(t)
    print(f"[{time.strftime('%X')}]slow 3 complete")
    assert False, f"This slow test needs {t}s"
