from pytest import mark


@mark.door
def test_door_open():
    print("Door is open.")
    assert True


@mark.door
def test_door_close():
    print("Door is close.")
    assert True
