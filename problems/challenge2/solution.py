"""
Program to calculate simple interest.

This module provides a function to calculate simple interest given principal, rate, and time.
Formula: SI = (P * R * T) / 100
"""

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Args:
        principal (float): Principal amount
        rate (float): Rate of interest per annum
        time (float): Time in years

    Returns:
        float: Simple interest amount
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

if __name__ == "__main__":
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (%): "))
        time = float(input("Enter time in years: "))
        si = calculate_simple_interest(principal, rate, time)
        print(f"Simple Interest: {si:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")