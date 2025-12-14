"""
Tests for Challenge 59: M*N matrix and transpose
"""

from solution import transpose_matrix

def test_transpose():
    matrix = [[1, 2], [3, 4]]
    transposed = transpose_matrix(matrix)
    assert transposed == [[1, 3], [2, 4]]

def test_single():
    matrix = [[5]]
    transposed = transpose_matrix(matrix)
    assert transposed == [[5]]

def test_empty():
    matrix = []
    transposed = transpose_matrix(matrix)
    assert transposed == []

def test_rectangular():
    matrix = [[1, 2, 3], [4, 5, 6]]
    transposed = transpose_matrix(matrix)
    assert transposed == [[1, 4], [2, 5], [3, 6]]