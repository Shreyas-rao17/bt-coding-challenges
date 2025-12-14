"""
Tax and Rebate Calculation.
"""

def calculate_tax_and_cess(taxable_income):
    """
    Calculate tax, rebate, cess.
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
    
    if taxable_income <= 700000:
        tax = 0
    
    cess = tax * 0.04
    total_tax = tax + cess
    
    return tax, cess, total_tax

if __name__ == "__main__":
    try:
        taxable = float(input("Enter taxable income: "))
        tax, cess, total = calculate_tax_and_cess(taxable)
        print(f"Tax: {tax:.2f}")
        print(f"Cess: {cess:.2f}")
        print(f"Total Tax Payable: {total:.2f}")
    except ValueError:
        print("Invalid input.")