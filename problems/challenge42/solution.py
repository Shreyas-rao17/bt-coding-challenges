import math

def print_factorials_pattern(n):
    """
    Print factorials pattern in N rows.
    
    Args:
        n (int): Number of rows
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    
    factorials = []
    for i in range(sum(range(1, n + 1))):
        factorials.append(math.factorial(i))
    
    idx = 0
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(str(factorials[idx]))
            idx += 1
        print(' '.join(row))

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        print_factorials_pattern(n)
    except ValueError as e:
        print(f"Error: {e}")