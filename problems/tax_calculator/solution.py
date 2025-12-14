"""
Tax Calculator for New Tax Regime (2023).
"""

def calculate_gross_salary(basic_monthly, special_allowances, bonus_percentage):
    """
    Calculate gross monthly and annual salary.
    """
    gross_monthly = basic_monthly + special_allowances
    annual_gross = 12 * gross_monthly / (1 - bonus_percentage / 100)
    return gross_monthly, annual_gross

def calculate_taxable_income(annual_gross):
    """
    Calculate taxable income after standard deduction.
    """
    standard_deduction = 50000
    taxable_income = max(0, annual_gross - standard_deduction)
    return taxable_income

def calculate_tax(taxable_income):
    """
    Calculate tax based on slabs, apply rebate and cess.
    """
    slabs = [
        (300000, 0),
        (600000, 0.05),
        (900000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float('inf'), 0.30)
    ]
    
    tax = 0
    remaining = taxable_income
    prev_limit = 0
    
    for limit, rate in slabs:
        if remaining > 0:
            taxable_in_slab = min(remaining, limit - prev_limit)
            tax += taxable_in_slab * rate
            remaining -= taxable_in_slab
            prev_limit = limit
        else:
            break
    
    # Rebate if taxable <= 700000
    if taxable_income <= 700000:
        tax = 0
    
    # Cess 4%
    cess = tax * 0.04
    total_tax = tax + cess
    
    return tax, cess, total_tax

def calculate_net_salary(annual_gross, total_tax):
    """
    Calculate net salary.
    """
    return annual_gross - total_tax

def generate_report(name, emp_id, basic_monthly, special_allowances, bonus_percentage):
    """
    Generate full tax report.
    """
    gross_monthly, annual_gross = calculate_gross_salary(basic_monthly, special_allowances, bonus_percentage)
    taxable_income = calculate_taxable_income(annual_gross)
    tax, cess, total_tax = calculate_tax(taxable_income)
    net_salary = calculate_net_salary(annual_gross, total_tax)
    
    report = f"""
Employee Tax Report
Name: {name}
EmpID: {emp_id}
Gross Monthly Salary: {gross_monthly:.2f}
Annual Gross Salary: {annual_gross:.2f}
Taxable Income: {taxable_income:.2f}
Tax Payable: {tax:.2f}
Cess: {cess:.2f}
Total Tax: {total_tax:.2f}
Annual Net Salary: {net_salary:.2f}
"""
    return report.strip()

if __name__ == "__main__":
    try:
        name = input("Enter name: ")
        emp_id = input("Enter EmpID: ")
        basic = float(input("Enter basic monthly salary: "))
        allowances = float(input("Enter special allowances: "))
        bonus_pct = float(input("Enter bonus percentage: "))
        
        report = generate_report(name, emp_id, basic, allowances, bonus_pct)
        print(report)
    except ValueError:
        print("Invalid input. Enter numeric values.")