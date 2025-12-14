def print_number_pattern(n):
    """
    Print a number pattern of N rows, each row containing 1 to N.
    
    Args:
        n (int): Number of rows and max number
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    
    pattern = ''.join(str(i) for i in range(1, n + 1))
    for _ in range(n):
        print(pattern)

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        print_number_pattern(n)
    except ValueError as e:
        print(f"Error: {e}")