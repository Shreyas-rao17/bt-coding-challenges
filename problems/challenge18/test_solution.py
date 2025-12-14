"""
Tests for odd series.
"""

from solution import generate_series

def test_n5():
    assert generate_series(5) == [1,3,5]

def test_n1():
    assert generate_series(1) == [1]

def test_n2():
    assert generate_series(2) == [1]