"""
Report Generation.
"""

def generate_report(name, emp_id, gross_monthly, annual_gross, taxable_income, tax_payable, net_salary):
    """
    Generate detailed report.
    """
    report = f"""
Employee Tax Report
Name: {name}
EmpID: {emp_id}
Gross Monthly Salary: {gross_monthly:.2f}
Annual Gross Salary: {annual_gross:.2f}
Taxable Income: {taxable_income:.2f}
Tax Payable: {tax_payable:.2f}
Annual Net Salary: {net_salary:.2f}
"""
    return report.strip()

if __name__ == "__main__":
    # Example values
    report = generate_report("John Doe", "E12345", 85000, 1020000, 970000, 76800, 943200)
    print(report)