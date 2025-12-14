"""
Find the largest of 3 numbers.
"""

def find_largest(a, b, c):
    """
    Find the largest of three numbers.

    Args:
        a, b, c (float): Numbers

    Returns:
        float: Largest number
    """
    return max(a, b, c)

if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))
        largest = find_largest(a, b, c)
        print(f"The largest number is {largest}.")
    except ValueError:
        print("Invalid input.")