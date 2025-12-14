"""
Tests for even or odd.
"""

from solution import is_even_or_odd

def test_even():
    assert is_even_or_odd(4) == "Even"

def test_odd():
    assert is_even_or_odd(5) == "Odd"

def test_zero():
    assert is_even_or_odd(0) == "Even"

def test_negative_even():
    assert is_even_or_odd(-2) == "Even"

def test_negative_odd():
    assert is_even_or_odd(-3) == "Odd"