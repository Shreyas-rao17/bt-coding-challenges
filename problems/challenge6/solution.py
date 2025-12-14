"""
Check if a number is even or odd.
"""

def is_even_or_odd(num):
    """
    Check if number is even or odd.

    Args:
        num (int): Number to check

    Returns:
        str: "Even" or "Odd"
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        result = is_even_or_odd(num)
        print(f"The number {num} is {result}.")
    except ValueError:
        print("Invalid input. Enter an integer.")