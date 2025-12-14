"""
Test cases for discount calculation.
"""

import pytest
from solution import calculate_discount

def test_normal_discount():
    discount, final = calculate_discount(1000, 10)
    assert discount == 100
    assert final == 900

def test_zero_discount():
    discount, final = calculate_discount(1000, 0)
    assert discount == 0
    assert final == 1000

def test_full_discount():
    discount, final = calculate_discount(1000, 100)
    assert discount == 1000
    assert final == 0

def test_fractional():
    discount, final = calculate_discount(100, 5.5)
    assert discount == 5.5
    assert final == 94.5

def test_negative_total():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)

def test_negative_percent():
    with pytest.raises(ValueError):
        calculate_discount(100, -10)

def test_over_100_percent():
    with pytest.raises(ValueError):
        calculate_discount(100, 110)