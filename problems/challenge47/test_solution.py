"""
Tests for Challenge 47: Accept n and store elements
"""

from solution import accept_array

def test_n0():
    try:
        accept_array(0)
        assert False
    except ValueError as e:
        assert "N must be a positive integer" in str(e)

def test_negative():
    try:
        accept_array(-1)
        assert False
    except ValueError as e:
        assert "N must be a positive integer" in str(e)

def test_float():
    try:
        accept_array(2.5)
        assert False
    except ValueError as e:
        assert "N must be a positive integer" in str(e)