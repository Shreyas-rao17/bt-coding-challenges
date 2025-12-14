"""
Tests for Challenge 30: Promotional Discounts on Specific Items
"""

from solution import calculate_item_total

def test_normal_item():
    total, discount = calculate_item_total("A001", "Apple", 2, 50.0)
    assert total == 100.0
    assert discount == 0.0

def test_promo_item():
    total, discount = calculate_item_total("PROMO10", "Banana", 2, 50.0)
    assert total == 90.0
    assert discount == 10.0

def test_promo_case_sensitive():
    total, discount = calculate_item_total("promo10", "Banana", 2, 50.0)
    assert total == 100.0  # No discount
    assert discount == 0.0

def test_promo_multiple():
    total, discount = calculate_item_total("PROMO10", "Orange", 3, 20.0)
    assert total == 54.0  # 60 - 6
    assert discount == 6.0