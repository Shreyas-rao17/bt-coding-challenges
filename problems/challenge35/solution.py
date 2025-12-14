def print_number_pattern(n):
    """
    Print a number pattern of N rows, row i has i repeated N times.
    
    Args:
        n (int): Number of rows
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    
    for i in range(1, n + 1):
        print(str(i) * n)

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        print_number_pattern(n)
    except ValueError as e:
        print(f"Error: {e}")