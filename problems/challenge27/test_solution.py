"""
Tests for Challenge 27: Applying Discounts
"""

from solution import calculate_item_total, calculate_grand_total, apply_discounts

def test_no_discount():
    grand_total, discount_amount, explanation = apply_discounts(5000, 10)
    assert grand_total == 5000
    assert discount_amount == 0
    assert explanation == []

def test_10_percent_discount():
    grand_total, discount_amount, explanation = apply_discounts(15000, 10)
    assert grand_total == 13500
    assert discount_amount == 1500
    assert len(explanation) == 1
    assert "10% discount applied: ₹1500.00" in explanation[0]

def test_quantity_discount():
    grand_total, discount_amount, explanation = apply_discounts(5000, 25)
    assert grand_total == 4750
    assert discount_amount == 250
    assert len(explanation) == 1
    assert "5% quantity discount applied: ₹250.00" in explanation[0]

def test_both_discounts():
    grand_total, discount_amount, explanation = apply_discounts(15000, 25)
    # First 10%: 15000 - 1500 = 13500
    # Then 5%: 13500 - 675 = 12825
    assert grand_total == 12825
    assert discount_amount == 2175
    assert len(explanation) == 2

def test_exactly_10000():
    grand_total, discount_amount, explanation = apply_discounts(10000, 10)
    assert grand_total == 10000
    assert discount_amount == 0

def test_exactly_20_quantity():
    grand_total, discount_amount, explanation = apply_discounts(5000, 20)
    assert grand_total == 5000
    assert discount_amount == 0