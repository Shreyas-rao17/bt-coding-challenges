"""
Tests for Challenge 48: Sum of elements
"""

from solution import sum_array

def test_positive():
    assert sum_array([1, 2, 3]) == 6

def test_negative():
    assert sum_array([-1, -2, -3]) == -6

def test_mixed():
    assert sum_array([1, -2, 3]) == 2

def test_empty():
    assert sum_array([]) == 0

def test_single():
    assert sum_array([5]) == 5