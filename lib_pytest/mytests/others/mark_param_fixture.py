import pytest

@pytest.fixture(params=[0, 1, 2, 3, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


@pytest.mark.params
def test_data(data_set):
    print(f"Test with data_set: {data_set}")
