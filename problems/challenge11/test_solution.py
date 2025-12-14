"""
Tests for basic salary calculation.
"""

import pytest
from solution import calculate_gross_salaries

def test_normal_calculation():
    gross_monthly, annual_gross = calculate_gross_salaries(50000, 10000, 10)
    assert gross_monthly == 60000
    assert annual_gross == 720000 + 72000  # 12*60000 + 10% of 12*60000

def test_zero_bonus():
    gross_monthly, annual_gross = calculate_gross_salaries(50000, 10000, 0)
    assert gross_monthly == 60000
    assert annual_gross == 720000

def test_high_bonus():
    gross_monthly, annual_gross = calculate_gross_salaries(50000, 10000, 20)
    assert gross_monthly == 60000
    assert annual_gross == 720000 + 144000  # 20% of 720000