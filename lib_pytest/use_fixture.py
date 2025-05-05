import pytest

@pytest.fixture
def fix_step():
    print("Start to my fix step.")


def test_my(fix_step):
    print("In test_my")
    assert 1 > 0
