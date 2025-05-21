import pytest

@pytest.fixture
def my_fixture():
    print("This is my fixture.")
    return 123

#@pytest.fixture(scope="session") # only "teardown" once
@pytest.fixture(scope="function")
def fixture_with_teardown():
    print("This is second fixture.")
    yield 456
    print("======> Teardown second fixture.")
