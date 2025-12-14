def print_number_increasing(n):
    """
    Print a number increasing pattern of N rows.
    
    Args:
        n (int): Number of rows
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    
    for i in range(1, n + 1):
        line = ''.join(str(j) for j in range(1, i + 1))
        print(line)

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        print_number_increasing(n)
    except ValueError as e:
        print(f"Error: {e}")