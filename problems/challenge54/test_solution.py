"""
Tests for Challenge 54: Sort array
"""

from solution import sort_array

def test_asc():
    assert sort_array([3, 1, 2], 'asc') == [1, 2, 3]

def test_desc():
    assert sort_array([3, 1, 2], 'desc') == [3, 2, 1]

def test_asc_case():
    assert sort_array([3, 1, 2], 'ASC') == [1, 2, 3]

def test_invalid_order():
    try:
        sort_array([1, 2], 'invalid')
        assert False
    except ValueError as e:
        assert "Order must be" in str(e)