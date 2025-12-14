"""
Tests for series 1,4,7,12,23...
"""

from solution import generate_series

def test_n23():
    assert generate_series(23) == [1,4,7,12,23]

def test_n10():
    assert generate_series(10) == [1,4,7]

def test_n1():
    assert generate_series(1) == [1]