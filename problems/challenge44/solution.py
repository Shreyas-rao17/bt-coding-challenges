def generate_series(n):
    """
    Generate the series 1, -5, 9, -13, ... up to N terms.
    
    Args:
        n (int): Number of terms
        
    Returns:
        list: The series
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    
    series = []
    for i in range(1, n + 1):
        sign = 1 if i % 2 == 1 else -1
        value = sign * (4 * i - 3)
        series.append(value)
    return series

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        series = generate_series(n)
        print(', '.join(map(str, series)))
    except ValueError as e:
        print(f"Error: {e}")