"""
Tests for Challenge 57: Sum of 2D array
"""

from solution import sum_2d_array

def test_normal():
    arr = [[1, 2], [3, 4]]
    assert sum_2d_array(arr) == 10

def test_single():
    arr = [[5]]
    assert sum_2d_array(arr) == 5

def test_empty():
    arr = []
    assert sum_2d_array(arr) == 0

def test_negative():
    arr = [[-1, 2], [3, -4]]
    assert sum_2d_array(arr) == 0