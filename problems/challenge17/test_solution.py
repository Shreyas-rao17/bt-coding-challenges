"""
Tests for series 1 to N.
"""

from solution import generate_series

def test_n5():
    assert generate_series(5) == [1,2,3,4,5]

def test_n1():
    assert generate_series(1) == [1]

def test_n0():
    assert generate_series(0) == []