import pytest
from src.math_operations import add, sub

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 3, 8),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (5, 8, -3),
])
def test_sub(a, b, expected):
    assert sub(a, b) == expected
