"""
Tests for net salary.
"""

from solution import calculate_net_salary

def test_normal():
    assert calculate_net_salary(1000000, 100000) == 900000

def test_zero_tax():
    assert calculate_net_salary(1000000, 0) == 1000000

def test_high_tax():
    assert calculate_net_salary(1000000, 500000) == 500000