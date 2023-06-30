import os
import pytest


def name_length(filename):
    if not os.path.isfile(filename):
        raise ValueError('{} is not a file!'.format(filename))
    print(filename)
    return len(filename)


def test_name_length0(mocker):
    isfile = mocker.patch('os.path.isfile', return_value=True)
    assert 4 == name_length('outp')
    isfile.assert_called_once()

    isfile.return_value = False
    with pytest.raises(ValueError):
        name_length('test')
    assert 2 == isfile.call_count


def test_name_length1(mocker):
    mocker.patch('os.path.isfile', side_effect=TypeError)
    with pytest.raises(TypeError):
        name_length('test')


def test_name_length2(mocker):
    mocker.patch('os.path.isfile', return_value=True)
#    mock_print = mocker.patch('builtins.print', wraps=print)
    print "--------: " +__name__
    mock_len = mocker.patch(__name__ + '.len', wraps=len)
    assert 4 == name_length('test')
#    assert mock_print.called
    assert mock_len.called
