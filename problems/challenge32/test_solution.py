"""
Tests for Challenge 32: Minimum Purchase Requirements
"""

from solution import check_minimum_purchase

def test_above_minimum():
    assert check_minimum_purchase(600) == True

def test_exactly_minimum():
    assert check_minimum_purchase(500) == True

def test_below_minimum():
    assert check_minimum_purchase(400) == False

def test_zero():
    assert check_minimum_purchase(0) == False

def test_negative():
    assert check_minimum_purchase(-100) == False