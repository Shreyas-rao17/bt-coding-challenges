"""
Tests for Challenge 53: Reverse array
"""

from solution import reverse_array

def test_normal():
    assert reverse_array([1, 2, 3]) == [3, 2, 1]

def test_single():
    assert reverse_array([5]) == [5]

def test_empty():
    assert reverse_array([]) == []

def test_even():
    assert reverse_array([1, 2, 3, 4]) == [4, 3, 2, 1]