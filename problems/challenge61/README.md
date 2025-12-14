# Challenge 61: Matrix Addition

Write a Python program to add two matrices.

## Requirements

- Function `add_matrices(matrix1, matrix2)` that takes two matrices as lists of lists and returns their sum.
- Validate that inputs are lists of lists with the same dimensions.
- Handle invalid inputs by raising ValueError.
- Include a `display_matrix(matrix)` function to print the matrix.
- In the main block, take user input for matrix dimensions and elements, add them, and display the result.

## Example

Input:
```
2
2
1 2
3 4
5 6
7 8
```

Output:
```
6 8
10 12
```

## Testing

Run `pytest test_solution.py` to execute the tests.