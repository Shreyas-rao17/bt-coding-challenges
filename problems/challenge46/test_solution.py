"""
Tests for Challenge 46: Reverse of a number
"""

from solution import reverse_number

def test_positive():
    assert reverse_number(123) == 321

def test_negative():
    assert reverse_number(-456) == -654

def test_zero():
    assert reverse_number(0) == 0

def test_single_digit():
    assert reverse_number(5) == 5

def test_with_zeros():
    assert reverse_number(100) == 1

def test_float():
    try:
        reverse_number(1.5)
        assert False
    except ValueError as e:
        assert "integer" in str(e)