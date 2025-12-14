"""
Tests for Challenge 45: Whole and Fraction value separation
"""

from solution import separate_whole_fraction

def test_positive():
    whole, frac = separate_whole_fraction(3.14)
    assert whole == 3
    assert abs(frac - 0.14) < 1e-10

def test_negative():
    whole, frac = separate_whole_fraction(-2.5)
    assert whole == -2
    assert abs(frac - (-0.5)) < 1e-10

def test_integer():
    whole, frac = separate_whole_fraction(5.0)
    assert whole == 5
    assert frac == 0.0

def test_zero():
    whole, frac = separate_whole_fraction(0.0)
    assert whole == 0
    assert frac == 0.0