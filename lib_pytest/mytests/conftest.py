import pytest

@pytest.fixture
def my_fixture():
    print("This is my fixture.")
    return 123
