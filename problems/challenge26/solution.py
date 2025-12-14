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
    print(f"\nGrand Total: ₹{grand_total:.2f}")
    print(f"Total Quantity: {total_quantity}")
    print("\nItems purchased:")
    for item in items:
        print(f"- {item['description']} (Code: {item['code']}): {item['quantity']} x ₹{item['price']:.2f} = ₹{item['total']:.2f}")