"""
Check if salary > 3L and display tax message.
"""

def check_tax_eligibility(name, salary):
    """
    Check if salary > 300000 and return tax message.

    Args:
        name (str): Person's name
        salary (float): Salary amount

    Returns:
        str: Tax eligibility message
    """
    if salary > 300000:
        return f"{name}, you must pay tax."
    else:
        return f"{name}, you do not need to pay tax."

if __name__ == "__main__":
    try:
        name = input("Enter name: ")
        salary = float(input("Enter salary: "))
        message = check_tax_eligibility(name, salary)
        print(message)
    except ValueError:
        print("Invalid input.")