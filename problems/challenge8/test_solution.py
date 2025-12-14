"""
Tests for largest of 3 numbers.
"""

from solution import find_largest

def test_first_largest():
    assert find_largest(5, 2, 3) == 5

def test_second_largest():
    assert find_largest(2, 7, 3) == 7

def test_third_largest():
    assert find_largest(2, 3, 8) == 8

def test_all_equal():
    assert find_largest(4, 4, 4) == 4

def test_negatives():
    assert find_largest(-1, -5, -3) == -1
    
def test_negatives():
    assert find_largest(-1, -5, 3) == 3