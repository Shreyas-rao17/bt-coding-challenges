"""
Program to swap two numbers.
"""

def swap_numbers(a, b):
    """
    Swap two numbers using a temporary variable.

    Args:
        a: First number
        b: Second number

    Returns:
        tuple: (swapped_a, swapped_b)
    """
    temp = a
    a = b
    b = temp
    return a, b

if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        a, b = swap_numbers(a, b)
        print(f"After swap: First = {a}, Second = {b}")
    except ValueError:
        print("Invalid input. Enter numbers.")