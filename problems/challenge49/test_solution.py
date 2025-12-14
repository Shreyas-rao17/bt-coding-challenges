"""
Tests for Challenge 49: Min value
"""

from solution import min_array

def test_positive():
    assert min_array([1, 2, 3]) == 1

def test_negative():
    assert min_array([-1, -2, -3]) == -3

def test_mixed():
    assert min_array([1, -2, 3]) == -2

def test_single():
    assert min_array([5]) == 5

def test_empty():
    try:
        min_array([])
        assert False
    except ValueError as e:
        assert "empty" in str(e)