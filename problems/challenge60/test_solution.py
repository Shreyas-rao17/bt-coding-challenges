"""
Tests for Challenge 60: Multiply two matrices
"""

from solution import multiply_matrices

def test_multiply():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    result = multiply_matrices(a, b)
    expected = [[19, 22], [43, 50]]
    assert result == expected

def test_invalid():
    a = [[1, 2]]
    b = [[1], [2], [3]]
    try:
        multiply_matrices(a, b)
        assert False
    except ValueError as e:
        assert "cannot be multiplied" in str(e)