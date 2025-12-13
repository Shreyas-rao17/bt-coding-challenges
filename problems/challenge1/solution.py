"""
Program to find the sum and average of two variables.
"""

def calculate_sum_and_average(a, b):
    """
    Calculate the sum and average of two numbers.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        tuple: (sum, average)
    """
    sum_val = a + b
    average = sum_val / 2
    return sum_val, average

if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        sum_val, average = calculate_sum_and_average(a, b)
        print(f"Sum: {sum_val}")
        print(f"Average: {average}")
    except ValueError:
        print("Invalid input. Please enter numbers.")