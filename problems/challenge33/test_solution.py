"""
Tests for Challenge 33: Loyalty Points
"""

from solution import calculate_loyalty_points

def test_100():
    assert calculate_loyalty_points(100) == 1

def test_250():
    assert calculate_loyalty_points(250) == 2

def test_99():
    assert calculate_loyalty_points(99) == 0

def test_1000():
    assert calculate_loyalty_points(1000) == 10

def test_0():
    assert calculate_loyalty_points(0) == 0

def test_199():
    assert calculate_loyalty_points(199) == 1