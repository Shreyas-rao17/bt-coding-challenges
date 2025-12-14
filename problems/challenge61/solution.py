def add_matrices(matrix1, matrix2):
    """
    Add two matrices.
    
    Args:
        matrix1 (list of lists): First matrix
        matrix2 (list of lists): Second matrix
        
    Returns:
        list of lists: Result matrix
        
    Raises:
        ValueError: If matrices have incompatible dimensions or invalid input
    """
    if not isinstance(matrix1, list) or not isinstance(matrix2, list):
        raise ValueError("Matrices must be lists of lists")
    
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty")
    
    # Check matrix1 structure
    if not all(isinstance(row, list) for row in matrix1):
        raise ValueError("Invalid matrix1 structure")
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    if not all(len(row) == cols1 for row in matrix1):
        raise ValueError("Invalid matrix1 structure")
    
    # Check matrix2 structure
    if not all(isinstance(row, list) for row in matrix2):
        raise ValueError("Invalid matrix2 structure")
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    if not all(len(row) == cols2 for row in matrix2):
        raise ValueError("Invalid matrix2 structure")
    
    if rows1 != rows2 or cols1 != cols2:
        raise ValueError("Matrices must have the same dimensions")
    
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def display_matrix(matrix):
    """
    Display a matrix.
    
    Args:
        matrix (list of lists): The matrix to display
    """
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    try:
        # For simplicity, hardcode or input, but since it's command line, perhaps input rows, cols, then elements
        # But to match others, perhaps assume input as in previous
        # For matrix, it's tricky in command line, so perhaps use the function directly
        # But to match, perhaps input two matrices as lists of lists, but that's hard.
        # Perhaps input dimensions and elements.
        print("Matrix Addition")
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        print("Enter matrix 1:")
        matrix1 = []
        for i in range(rows):
            row = list(map(int, input().split()))
            if len(row) != cols:
                raise ValueError("Invalid row length")
            matrix1.append(row)
        
        print("Enter matrix 2:")
        matrix2 = []
        for i in range(rows):
            row = list(map(int, input().split()))
            if len(row) != cols:
                raise ValueError("Invalid row length")
            matrix2.append(row)
        
        result = add_matrices(matrix1, matrix2)
        print("Result:")
        display_matrix(result)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")