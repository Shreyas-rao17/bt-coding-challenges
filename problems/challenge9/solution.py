"""
Check if a year is a leap year.
"""

def is_leap_year(year):
    """
    Check if year is leap year.

    Args:
        year (int): Year

    Returns:
        bool: True if leap year
    """
    if year < 0:
        raise ValueError("Year cannot be negative")

    # Leap year logic. Must be divisible by 4, not divisible by 100 unless also divisible by 400. 
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

if __name__ == "__main__":
    try:
        year = int(input("Enter year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input.")