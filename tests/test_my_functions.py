import pytest
import time
import source.my_functions as my_functions


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5


def test_divide():
    result = my_functions.divide(1, 4)
    assert result == 0.25


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2


@pytest.mark.skip(reason="Not implemented yet")
def test_add():
    assert my_functions.add(1, 2) == 3


@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_by_zero():
    my_functions.divide(4, 0)
