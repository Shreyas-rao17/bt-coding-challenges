"""
Tests for Challenge 44: Generate Series
"""

from solution import generate_series

def test_n1():
    assert generate_series(1) == [1]

def test_n6():
    assert generate_series(6) == [1, -5, 9, -13, 17, -21]

def test_n10():
    series = generate_series(10)
    assert len(series) == 10
    assert series[0] == 1
    assert series[1] == -5
    assert series[2] == 9

def test_n0():
    try:
        generate_series(0)
        assert False
    except ValueError as e:
        assert "N must be a positive integer" in str(e)