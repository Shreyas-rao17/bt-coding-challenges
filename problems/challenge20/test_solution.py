"""
Tests for cumulative series.
"""

from solution import generate_series

def test_n22():
    assert generate_series(22) == [1,2,4,7,11,16,22]

def test_n5():
    assert generate_series(5) == [1,2,4]

def test_n0():
    assert generate_series(0) == []