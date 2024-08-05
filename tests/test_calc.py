import pytest
from calc import *


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0


def test_substract():
    assert substract(2, 3) == -1
    assert substract(-2, 3) == -5
    assert substract(0, 0) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 0) == 0


def test_divide():
    assert divide(6, 2) == 3
    assert divide(-6, 3) == -2
    assert divide(0, 5) == 0
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)
