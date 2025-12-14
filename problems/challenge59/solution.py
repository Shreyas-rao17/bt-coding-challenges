def create_matrix(m, n):
    """
    Create M x N matrix.
    
    Args:
        m (int): Rows
        n (int): Cols
        
    Returns:
        list: Matrix
    """
    if not isinstance(m, int) or m <= 0 or not isinstance(n, int) or n <= 0:
        raise ValueError("M and N must be positive integers")
    
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            elem = int(input(f"Enter element [{i}][{j}]: "))
            row.append(elem)
        matrix.append(row)
    return matrix

def transpose_matrix(matrix):
    """
    Transpose the matrix.
    
    Args:
        matrix (list): 2D list
        
    Returns:
        list: Transposed matrix
    """
    if not matrix:
        return []
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def display_matrix(matrix):
    """
    Display matrix.
    
    Args:
        matrix (list): 2D list
    """
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    try:
        m = int(input("Enter M (rows): "))
        n = int(input("Enter N (cols): "))
        matrix = create_matrix(m, n)
        print("Matrix:")
        display_matrix(matrix)
        transposed = transpose_matrix(matrix)
        print("Transpose:")
        display_matrix(transposed)
    except ValueError as e:
        print(f"Error: {e}")