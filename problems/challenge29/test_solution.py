"""
Tests for Challenge 29: Tax Calculation Based on Purchase Amount
"""

from solution import calculate_tax

def test_tax_low():
    tax_amount, tax_rate = calculate_tax(3000)
    assert tax_amount == 150
    assert tax_rate == 0.05

def test_tax_medium():
    tax_amount, tax_rate = calculate_tax(10000)
    assert tax_amount == 1000
    assert tax_rate == 0.10

def test_tax_high():
    tax_amount, tax_rate = calculate_tax(25000)
    assert tax_amount == 3750
    assert tax_rate == 0.15

def test_tax_boundary_low():
    tax_amount, tax_rate = calculate_tax(4999.99)
    assert tax_amount == 249.9995
    assert tax_rate == 0.05

def test_tax_boundary_medium():
    tax_amount, tax_rate = calculate_tax(5000)
    assert tax_amount == 500
    assert tax_rate == 0.10

def test_tax_boundary_high():
    tax_amount, tax_rate = calculate_tax(20000)
    assert tax_amount == 2000
    assert tax_rate == 0.10

def test_tax_above_high():
    tax_amount, tax_rate = calculate_tax(20000.01)
    assert tax_amount == 3000.0015
    assert tax_rate == 0.15