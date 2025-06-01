from pytest import mark


@mark.engine
def test_engine_start(my_fixture):
    print("Engine is started.")
    assert True


@mark.engine
def test_engine_running(fixture_with_teardown):
    print("Engine is running:", fixture_with_teardown)
    assert True


@mark.engine
def test_engine_stop(fixture_with_teardown):
    print("Engine is stopped:", fixture_with_teardown)
    a = 123
    b = 123
    assert a == b


@mark.engine
def test_always_fail():
    a = 123
    b = {"name": "Tom"}
    c = '123'
    print("This case should be failed(1).")
    assert a == c
    assert a == b
    print("This case should be failed(2).")
