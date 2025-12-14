"""
Tests for Challenge 50: Max value
"""

from solution import max_array

def test_positive():
    assert max_array([1, 2, 3]) == 3

def test_negative():
    assert max_array([-1, -2, -3]) == -1

def test_mixed():
    assert max_array([1, -2, 3]) == 3

def test_single():
    assert max_array([5]) == 5

def test_empty():
    try:
        max_array([])
        assert False
    except ValueError as e:
        assert "empty" in str(e)