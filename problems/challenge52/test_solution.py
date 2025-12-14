"""
Tests for Challenge 52: Odd even count
"""

from solution import count_odd_even

def test_mixed():
    odd, even = count_odd_even([1, 2, 3, 4, 5])
    assert odd == 3
    assert even == 2

def test_all_odd():
    odd, even = count_odd_even([1, 3, 5])
    assert odd == 3
    assert even == 0

def test_all_even():
    odd, even = count_odd_even([2, 4, 6])
    assert odd == 0
    assert even == 3

def test_empty():
    odd, even = count_odd_even([])
    assert odd == 0
    assert even == 0

def test_zero():
    odd, even = count_odd_even([0])
    assert odd == 0
    assert even == 1