"""
Net Salary Calculation.
"""

def calculate_net_salary(annual_gross, total_tax):
    """
    Calculate net salary.
    """
    return annual_gross - total_tax

if __name__ == "__main__":
    try:
        gross = float(input("Enter annual gross salary: "))
        tax = float(input("Enter total tax payable: "))
        net = calculate_net_salary(gross, tax)
        print(f"Annual Gross Salary: {gross:.2f}")
        print(f"Total Tax Payable: {tax:.2f}")
        print(f"Annual Net Salary: {net:.2f}")
    except ValueError:
        print("Invalid input.")