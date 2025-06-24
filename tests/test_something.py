from main import *


def test_add1():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract1():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply1():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10