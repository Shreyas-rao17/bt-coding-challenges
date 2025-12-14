def print_star_pattern(n):
    """
    Print a star pattern of N rows, each with N stars.
    
    Args:
        n (int): Number of rows and stars per row
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    
    for _ in range(n):
        print('*' * n)

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        print_star_pattern(n)
    except ValueError as e:
        print(f"Error: {e}")