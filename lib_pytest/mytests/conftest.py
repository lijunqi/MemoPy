from pytest import fixture

@fixture
def my_fixture():
    print("This is my fixture.")
    return 123

#@fixture(scope="session") # only "teardown" once
@fixture(scope="function")
def fixture_with_teardown():
    print("This is second fixture.")
    yield 456
    print("======> Teardown second fixture.")


"""
    pytest --env=xxx
"""
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="DefaultEnv",
        help="Environment to run my test"
    )

@fixture(scope="session")
def env(request):
    res = request.config.getoption("--env")
    print("... In env ... : ", res)
    return res
