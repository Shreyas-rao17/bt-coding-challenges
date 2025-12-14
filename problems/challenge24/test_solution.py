"""
Tests for Fibonacci series.
"""

from solution import generate_series

def test_n21():
    assert generate_series(21) == [1,1,2,3,5,8,13,21]

def test_n5():
    assert generate_series(5) == [1,1,2,3,5]

def test_n1():
    assert generate_series(1) == [1,1]