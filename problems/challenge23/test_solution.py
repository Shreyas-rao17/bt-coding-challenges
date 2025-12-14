"""
Tests for series 1,5,9,13,21,25,29,37,41...
"""

from solution import generate_series

def test_n41():
    assert generate_series(41) == [1,5,9,13,21,25,29,37,41]

def test_n10():
    assert generate_series(10) == [1,5,9]

def test_n1():
    assert generate_series(1) == [1]