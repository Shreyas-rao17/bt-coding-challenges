"""
Tests for taxable income.
"""

from solution import calculate_taxable_income

def test_above_deduction():
    assert calculate_taxable_income(600000) == 550000

def test_equal_deduction():
    assert calculate_taxable_income(50000) == 0

def test_below_deduction():
    assert calculate_taxable_income(30000) == 0