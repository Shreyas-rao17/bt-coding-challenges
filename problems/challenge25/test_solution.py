"""
Tests for Challenge 25: Basic Item Entry and Total Calculation
"""

from solution import calculate_item_total

def test_valid_calculation():
    assert calculate_item_total("A001", "Apple", 2, 50.0) == 100.0

def test_quantity_zero():
    try:
        calculate_item_total("A001", "Apple", 0, 50.0)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "Quantity must be a positive integer" in str(e)

def test_negative_quantity():
    try:
        calculate_item_total("A001", "Apple", -1, 50.0)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "Quantity must be a positive integer" in str(e)

def test_price_zero():
    try:
        calculate_item_total("A001", "Apple", 2, 0)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "Price must be a positive number" in str(e)

def test_negative_price():
    try:
        calculate_item_total("A001", "Apple", 2, -10.0)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "Price must be a positive number" in str(e)

def test_empty_code():
    try:
        calculate_item_total("", "Apple", 2, 50.0)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "Code and description cannot be empty" in str(e)

def test_empty_description():
    try:
        calculate_item_total("A001", "", 2, 50.0)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "Code and description cannot be empty" in str(e)

def test_float_price():
    assert calculate_item_total("A001", "Apple", 3, 10.5) == 31.5