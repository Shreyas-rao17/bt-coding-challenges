"""
Taxable Income Calculation.
"""

def calculate_taxable_income(annual_gross):
    """
    Calculate taxable income after standard deduction.
    """
    standard_deduction = 50000
    taxable_income = max(0, annual_gross - standard_deduction)
    return taxable_income

if __name__ == "__main__":
    try:
        gross = float(input("Enter annual gross salary: "))
        taxable = calculate_taxable_income(gross)
        print(f"Gross Salary: {gross:.2f}")
        print(f"Standard Deduction: 50000.00")
        print(f"Taxable Income: {taxable:.2f}")
    except ValueError:
        print("Invalid input.")