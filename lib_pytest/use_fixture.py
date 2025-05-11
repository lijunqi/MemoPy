import pytest

@pytest.fixture
def fix_step():
    print(">>> Start to my fix step.")
    yield 123
    print("<<< End my fix step.")


def test_my(fix_step):
    print("In test_my")
    print("fix_step returns ", fix_step)
    assert 1 > 0
