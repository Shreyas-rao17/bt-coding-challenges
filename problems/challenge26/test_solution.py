"""
Tests for Challenge 26: Iterative Item Entry and Grand Total
"""

from solution import calculate_item_total, calculate_grand_total

def test_calculate_item_total():
    assert calculate_item_total("A001", "Apple", 2, 50.0) == 100.0

def test_calculate_grand_total():
    items = [
        {'quantity': 2, 'price': 50.0},
        {'quantity': 1, 'price': 100.0}
    ]
    grand_total, total_quantity = calculate_grand_total(items)
    assert grand_total == 200.0
    assert total_quantity == 3

def test_empty_items():
    grand_total, total_quantity = calculate_grand_total([])
    assert grand_total == 0.0
    assert total_quantity == 0

def test_single_item_grand_total():
    items = [{'quantity': 5, 'price': 20.0}]
    grand_total, total_quantity = calculate_grand_total(items)
    assert grand_total == 100.0
    assert total_quantity == 5