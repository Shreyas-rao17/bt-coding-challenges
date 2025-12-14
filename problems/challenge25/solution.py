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

if __name__ == "__main__":
    try:
        code = input("Enter item code: ").strip()
        description = input("Enter item description: ").strip()
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        
        total = calculate_item_total(code, description, quantity, price)
        print(f"Total cost for {description} (Code: {code}): ₹{total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")