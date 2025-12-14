def print_perfect_squares_pattern(n):
    """
    Print perfect squares with alternating signs in N rows.
    
    Args:
        n (int): Number of rows
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    
    squares = []
    sign = 1
    for i in range(1, sum(range(1, n + 1)) + 1):
        sq = i ** 2
        squares.append(sign * sq)
        sign = -sign
    
    idx = 0
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(str(squares[idx]))
            idx += 1
        print(' '.join(row))

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        print_perfect_squares_pattern(n)
    except ValueError as e:
        print(f"Error: {e}")