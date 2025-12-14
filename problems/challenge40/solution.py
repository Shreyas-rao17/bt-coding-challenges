def print_fibonacci_pattern(n):
    """
    Print Fibonacci series pattern of N rows.
    
    Args:
        n (int): Number of rows
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    
    fib = []
    a, b = 1, 1
    for _ in range(sum(range(1, n + 1))):  # Total numbers needed
        fib.append(a)
        a, b = b, a + b
    
    idx = 0
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(str(fib[idx]))
            idx += 1
        print(' '.join(row))

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        print_fibonacci_pattern(n)
    except ValueError as e:
        print(f"Error: {e}")