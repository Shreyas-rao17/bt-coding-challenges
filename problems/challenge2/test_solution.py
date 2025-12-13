"""
Test cases for the simple interest calculation program.

This module contains comprehensive test cases covering positive, negative,
and edge scenarios for the calculate_simple_interest function.
"""

import pytest
from solution import calculate_simple_interest

def test_positive_values():
    """Test with positive values."""
    si = calculate_simple_interest(1000, 5, 2)
    assert si == 100.0

def test_zero_principal():
    """Test with zero principal."""
    si = calculate_simple_interest(0, 5, 2)
    assert si == 0.0

def test_zero_rate():
    """Test with zero rate."""
    si = calculate_simple_interest(1000, 0, 2)
    assert si == 0.0

def test_zero_time():
    """Test with zero time."""
    si = calculate_simple_interest(1000, 5, 0)
    assert si == 0.0

def test_fractional_values():
    """Test with fractional values."""
    si = calculate_simple_interest(1000.5, 5.5, 2.5)
    expected = (1000.5 * 5.5 * 2.5) / 100
    assert abs(si - expected) < 1e-10

def test_large_numbers():
    """Test with large numbers."""
    si = calculate_simple_interest(1000000, 10, 5)
    assert si == 500000.0

def test_negative_values():
    """Test with negative values (edge case)."""
    si = calculate_simple_interest(-1000, 5, 2)
    assert si == -100.0

def test_mixed_negative():
    """Test with mixed negative values."""
    si = calculate_simple_interest(1000, -5, 2)
    assert si == -100.0

def test_invalid_type():
    """Test with invalid input types."""
    with pytest.raises(TypeError):
        calculate_simple_interest("abc", 5, 2)
