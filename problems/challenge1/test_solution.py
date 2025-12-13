"""
Test cases for the sum and average calculation program.

This module contains comprehensive test cases covering positive, negative,
and edge scenarios for the calculate_sum_and_average function.
"""

import pytest
from solution import calculate_sum_and_average

def test_positive_integers():
    """Test with positive integers."""
    sum_val, avg = calculate_sum_and_average(5, 10)
    assert sum_val == 15
    assert avg == 7.5

def test_negative_integers():
    """Test with negative integers."""
    sum_val, avg = calculate_sum_and_average(-5, -10)
    assert sum_val == -15
    assert avg == -7.5

def test_mixed_signs():
    """Test with one positive and one negative."""
    sum_val, avg = calculate_sum_and_average(5, -3)
    assert sum_val == 2
    assert avg == 1.0

def test_zero_values():
    """Test with zeros."""
    sum_val, avg = calculate_sum_and_average(0, 0)
    assert sum_val == 0
    assert avg == 0.0

def test_floats():
    """Test with floating point numbers."""
    sum_val, avg = calculate_sum_and_average(2.5, 3.5)
    assert sum_val == 6.0
    assert avg == 3.0

def test_large_numbers():
    """Test with large numbers."""
    sum_val, avg = calculate_sum_and_average(1000000, 2000000)
    assert sum_val == 3000000
    assert avg == 1500000.0

def test_small_floats():
    """Test with small floating point numbers."""
    sum_val, avg = calculate_sum_and_average(0.1, 0.2)
    assert abs(sum_val - 0.3) < 1e-10  # Due to floating point precision
    assert abs(avg - 0.15) < 1e-10
    
def test_invalid_input_type():
    """Test with invalid input types."""
    with pytest.raises(TypeError):
        calculate_sum_and_average("a", 5)
