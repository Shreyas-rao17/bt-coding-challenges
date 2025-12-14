def multiply_matrices(a, b):
    """
    Multiply two matrices.
    
    Args:
        a (list): Matrix A
        b (list): Matrix B
        
    Returns:
        list: Result matrix
        
    Raises:
        ValueError: If dimensions don't match
    """
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("Matrices cannot be multiplied")
    
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def display_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    try:
        # For simplicity, assume 2x2
        print("Matrix A:")
        a = []
        for i in range(2):
            row = []
            for j in range(2):
                elem = int(input(f"A[{i}][{j}]: "))
                row.append(elem)
            a.append(row)
        
        print("Matrix B:")
        b = []
        for i in range(2):
            row = []
            for j in range(2):
                elem = int(input(f"B[{i}][{j}]: "))
                row.append(elem)
            b.append(row)
        
        result = multiply_matrices(a, b)
        print("Result:")
        display_matrix(result)
    except ValueError as e:
        print(f"Error: {e}")