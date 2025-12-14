def calculate_item_total(code, description, quantity, price):
    """
    Calculate the total cost for a single item.
    
    Args:
        code (str): Item code
        description (str): Item description
        quantity (int): Quantity purchased
        price (float): Price per unit
        
    Returns:
        float: Total cost for the item
        
    Raises:
        ValueError: If quantity or price is invalid
    """
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer")
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError("Price must be a positive number")
    if not code or not description:
        raise ValueError("Code and description cannot be empty")
    
    total = quantity * price
    return total

def calculate_grand_total(items):
    """
    Calculate grand total from list of items.
    
    Args:
        items (list): List of dicts with 'quantity' and 'price'
        
    Returns:
        tuple: (grand_total, total_quantity)
    """
    grand_total = 0.0
    total_quantity = 0
    for item in items:
        item_total = item['quantity'] * item['price']
        grand_total += item_total
        total_quantity += item['quantity']
    return grand_total, total_quantity

def apply_discounts(grand_total, total_quantity):
    """
    Apply discounts based on rules.
    
    Args:
        grand_total (float): Original grand total
        total_quantity (int): Total quantity
        
    Returns:
        tuple: (discounted_total, discount_amount, explanation)
    """
    discount_amount = 0.0
    explanation = []
    
    if grand_total > 10000:
        discount = grand_total * 0.10
        discount_amount += discount
        grand_total -= discount
        explanation.append(f"10% discount applied: ₹{discount:.2f}")
    
    if total_quantity > 20:
        discount = grand_total * 0.05
        discount_amount += discount
        grand_total -= discount
        explanation.append(f"5% quantity discount applied: ₹{discount:.2f}")
    
    return grand_total, discount_amount, explanation

def apply_membership_discount(grand_total, is_member):
    """
    Apply membership discount if applicable.
    
    Args:
        grand_total (float): Grand total after other discounts
        is_member (bool): Whether customer is a member
        
    Returns:
        tuple: (final_total, discount_amount, explanation)
    """
    if is_member:
        discount = grand_total * 0.02
        grand_total -= discount
        return grand_total, discount, f"2% membership discount applied: ₹{discount:.2f}"
    return grand_total, 0.0, ""

def calculate_tax(grand_total):
    """
    Calculate tax based on grand total after discounts.
    
    Args:
        grand_total (float): Grand total after discounts
        
    Returns:
        tuple: (tax_amount, tax_rate)
    """
    if grand_total < 5000:
        tax_rate = 0.05
    elif grand_total <= 20000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15
    
    tax_amount = grand_total * tax_rate
    return tax_amount, tax_rate

if __name__ == "__main__":
    items = []
    while True:
        try:
            code = input("Enter item code (or 'done' to finish): ").strip()
            if code.lower() == 'done':
                break
            description = input("Enter item description: ").strip()
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
            
            item_total = calculate_item_total(code, description, quantity, price)
            items.append({
                'code': code,
                'description': description,
                'quantity': quantity,
                'price': price,
                'total': item_total
            })
            print(f"Item added. Total for this item: ₹{item_total:.2f}")
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")
    
    grand_total, total_quantity = calculate_grand_total(items)
    print(f"\nOriginal Grand Total: ₹{grand_total:.2f}")
    print(f"Total Quantity: {total_quantity}")
    
    discounted_total, discount_amount, explanation = apply_discounts(grand_total, total_quantity)
    print(f"Discounts Applied: ₹{discount_amount:.2f}")
    for exp in explanation:
        print(f"- {exp}")
    
    is_member = input("Are you a member? (y/n): ").strip().lower() == 'y'
    after_membership, membership_discount, membership_exp = apply_membership_discount(discounted_total, is_member)
    if membership_discount > 0:
        print(f"- {membership_exp}")
    
    tax_amount, tax_rate = calculate_tax(after_membership)
    final_total = after_membership + tax_amount
    print(f"Tax Applied ({tax_rate*100:.0f}%): ₹{tax_amount:.2f}")
    print(f"Final Grand Total (including tax): ₹{final_total:.2f}")
    
    print("\nItems purchased:")
    for item in items:
        print(f"- {item['description']} (Code: {item['code']}): {item['quantity']} x ₹{item['price']:.2f} = ₹{item['total']:.2f}")