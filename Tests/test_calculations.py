from app.calculations import *
import pytest

@pytest.mark.parametrize("x, y, res", [
    (3, 6, 9),
    (7, 1, 8),
    (12, 65, 77)
])
def test_add(x, y, res):
    print("testing add function")
    assert add(x, y) == res

def test_sub():
    assert sub(9, 5) == 4

def test_mul():
    assert mul(9, 5) == 45

def test_div():
    assert div(9, 3) == 3