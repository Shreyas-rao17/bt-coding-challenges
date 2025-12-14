"""
Tests for leap year.
"""
import pytest
from solution import is_leap_year

def test_leap_year():
    assert is_leap_year(2020) == True

def test_non_leap():
    assert is_leap_year(2021) == False

def test_century_leap():
    assert is_leap_year(2000) == True

def test_century_non_leap():
    assert is_leap_year(1900) == False
    
def test_negative_year_raises_error():
    with pytest.raises(ValueError):
        is_leap_year(-1900)

def test_2100():
    assert is_leap_year(2100) == False