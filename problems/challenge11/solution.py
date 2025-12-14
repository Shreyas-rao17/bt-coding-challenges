"""
Basic Input and Salary Calculation.
"""

def calculate_gross_salaries(basic_monthly, special_allowances, bonus_percentage):
    """
    Calculate gross monthly and annual salaries.
    """
    gross_monthly = basic_monthly + special_allowances
    bonus = gross_monthly * 12 * bonus_percentage / 100
    annual_gross = gross_monthly * 12 + bonus
    return gross_monthly, annual_gross

if __name__ == "__main__":
    try:
        name = input("Enter name: ")
        emp_id = input("Enter EmpID: ")
        basic = float(input("Enter basic monthly salary: "))
        allowances = float(input("Enter special allowances: "))
        bonus_pct = float(input("Enter bonus percentage: "))
        
        gross_monthly, annual_gross = calculate_gross_salaries(basic, allowances, bonus_pct)
        
        print(f"Name: {name}")
        print(f"EmpID: {emp_id}")
        print(f"Gross Monthly Salary: {gross_monthly:.2f}")
        print(f"Annual Gross Salary: {annual_gross:.2f}")
    except ValueError:
        print("Invalid input.")