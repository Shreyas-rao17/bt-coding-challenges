"""
Input Validation Rules.
"""

import re

def validate_inputs(name, emp_id, basic_salary, special_allowances, bonus_percentage):
    """
    Validate all inputs.
    """
    errors = []
    
    # Name: Non-empty, alphabets only, max 50
    if not name or not re.match(r'^[a-zA-Z\s]+$', name) or len(name) > 50:
        errors.append("Name must be non-empty, alphabets only, max 50 characters.")
    
    # EmpID: Alphanumeric, 5-10
    if not re.match(r'^[a-zA-Z0-9]{5,10}$', emp_id):
        errors.append("EmpID must be alphanumeric, 5-10 characters.")
    
    # Basic Salary: Positive, max 1e8
    try:
        basic = float(basic_salary)
        if basic <= 0 or basic > 100000000:
            errors.append("Basic salary must be positive, max 1,00,00,000.")
    except ValueError:
        errors.append("Basic salary must be a number.")
    
    # Special Allowances: Non-negative, max 1e8
    try:
        allowances = float(special_allowances)
        if allowances < 0 or allowances > 100000000:
            errors.append("Special allowances must be non-negative, max 1,00,00,000.")
    except ValueError:
        errors.append("Special allowances must be a number.")
    
    # Bonus Percentage: 0-100
    try:
        bonus = float(bonus_percentage)
        if not (0 <= bonus <= 100):
            errors.append("Bonus percentage must be 0-100.")
    except ValueError:
        errors.append("Bonus percentage must be a number.")
    
    return errors

if __name__ == "__main__":
    name = input("Enter name: ")
    emp_id = input("Enter EmpID: ")
    basic = input("Enter basic salary: ")
    allowances = input("Enter special allowances: ")
    bonus = input("Enter bonus percentage: ")
    
    errors = validate_inputs(name, emp_id, basic, allowances, bonus)
    if errors:
        for error in errors:
            print(f"Error: {error}")
    else:
        print("All inputs are valid.")