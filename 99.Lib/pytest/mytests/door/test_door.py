from pytest import mark


@mark.door
def test_door_open(env):
    print("Door is open. Env:", env)
    assert True


@mark.door
def test_door_close(env):
    print("Door is close. Env:", env)
    assert True
