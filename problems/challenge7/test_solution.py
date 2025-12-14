"""
Tests for tax eligibility.
"""

from solution import check_tax_eligibility

def test_above_threshold():
    assert "John, you must pay tax." in check_tax_eligibility("John", 350000)

def test_below_threshold():
    assert "Jane, you do not need to pay tax." in check_tax_eligibility("Jane", 250000)

def test_equal_threshold():
    assert "Bob, you do not need to pay tax." in check_tax_eligibility("Bob", 300000)