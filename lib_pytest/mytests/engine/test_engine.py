from pytest import mark


@mark.engine
def test_engine_start(my_fixture):
    print("Engine is started.")
    assert True


@mark.engine
def test_engine_stop():
    print("Engine is stopped.")
    assert True
