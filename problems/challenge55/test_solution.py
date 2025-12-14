"""
Tests for Challenge 55: Binary search
"""

from solution import binary_search

def test_found():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2

def test_not_found():
    assert binary_search([1, 2, 3, 4, 5], 6) == -1

def test_first():
    assert binary_search([1, 2, 3], 1) == 0

def test_last():
    assert binary_search([1, 2, 3], 3) == 2

def test_empty():
    assert binary_search([], 1) == -1

def test_single_found():
    assert binary_search([5], 5) == 0

def test_single_not():
    assert binary_search([5], 1) == -1