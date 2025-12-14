import pytest
from solution import add_matrices

def test_add():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert add_matrices(matrix1, matrix2) == expected

def test_invalid_dimensions():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6]]
    with pytest.raises(ValueError, match="Matrices must have the same dimensions"):
        add_matrices(matrix1, matrix2)

def test_empty_matrix():
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices([], [[1]])

def test_invalid_structure():
    with pytest.raises(ValueError, match="Invalid matrix1 structure"):
        add_matrices([[1], [2, 3]], [[4, 5], [6, 7]])