from pytest import mark


@mark.wheel
class TestWheel:
    def test_wheel_good(self):
        print("Wheel is good.")
        assert True

    def test_wheel_bad(self):
        print("Wheel is bad.")
        assert True
