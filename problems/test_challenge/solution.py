'''
Generate the pattern 5, 6, 7, 9, 12, 17, 25, 38, 59, 93,148, 237, 381, 614, 991

'''
def generate_pattern(n):
    """
    Generate a pattern of numbers where each number is the sum of the two preceding ones,
    starting from 5 and 6.

    Args:
        n (int): Number of terms to generate

    Returns:
        list: List containing the generated pattern

    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")

    pattern = []
    a, b = 5, 6
    for _ in range(n):
        pattern.append(a)
        a, b = b, a + b

    return pattern

if __name__ == "__main__":
    try:
        n = int(input("Enter number of terms to generate: "))
        pattern = generate_pattern(n)
        print(f"Generated pattern: {pattern}")
    except ValueError as e:
        print(f"Error: {e}")
    
    