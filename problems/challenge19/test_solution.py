"""
Tests for squares of evens.
"""

from solution import generate_series

def test_n64():
    assert generate_series(64) == [4,16,36,64]

def test_n10():
    assert generate_series(10) == [4]

def test_n3():
    assert generate_series(3) == []