import pytest

DATA_SET = [
    (1, 2, 2), (3, 4, 12), (5, 6, 30), (7, 8, 56), (9, 10, 90)
]


@pytest.mark.parametrize("a, b, c", DATA_SET)
def test_foo(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")
    assert a * b == c
