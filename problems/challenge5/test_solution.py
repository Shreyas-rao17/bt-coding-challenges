"""
Test cases for farmer sales calculation.
"""

from solution import calculate_farmer_sales

def test_total_sales():
    total, _ = calculate_farmer_sales()
    assert total == 14972800  # Calculated manually

def test_chemical_free_sales():
    _, cf = calculate_farmer_sales()
    assert cf == 12092800