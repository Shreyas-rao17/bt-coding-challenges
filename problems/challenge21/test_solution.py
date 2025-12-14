"""
Tests for squares excluding multiples of 4.
"""

from solution import generate_series

def test_n81():
    assert generate_series(81) == [1,4,9,25,36,49,81]

def test_n10():
    assert generate_series(10) == [1,4,9]

def test_n0():
    assert generate_series(0) == []