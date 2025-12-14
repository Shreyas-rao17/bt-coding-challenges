"""
Tests for Challenge 58: Check element in 2D array
"""

from solution import search_2d_array

def test_found():
    arr = [[1, 2], [3, 4]]
    assert search_2d_array(arr, 3) == True

def test_not_found():
    arr = [[1, 2], [3, 4]]
    assert search_2d_array(arr, 5) == False

def test_empty():
    arr = []
    assert search_2d_array(arr, 1) == False

def test_single():
    arr = [[5]]
    assert search_2d_array(arr, 5) == True