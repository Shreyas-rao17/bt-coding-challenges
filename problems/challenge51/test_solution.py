"""
Tests for Challenge 51: Search element
"""

from solution import search_element

def test_found():
    assert search_element([1, 2, 3], 2) == 1

def test_not_found():
    assert search_element([1, 2, 3], 4) == -1

def test_first():
    assert search_element([5, 2, 3], 5) == 0

def test_last():
    assert search_element([1, 2, 5], 5) == 2

def test_empty():
    assert search_element([], 1) == -1

def test_duplicates():
    assert search_element([1, 2, 2, 3], 2) == 1  # First occurrence