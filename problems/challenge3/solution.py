"""
Program to calculate discount on total amount.
"""

def calculate_discount(total, discount_percent):
    """
    Calculate discount amount and final price.

    Args:
        total (float): Total amount
        discount_percent (float): Discount percentage

    Returns:
        tuple: (discount_amount, final_amount)
    """
    if total < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid inputs")
    discount = (total * discount_percent) / 100
    final = total - discount
    return discount, final

if __name__ == "__main__":
    try:
        total = float(input("Enter total amount: "))
        discount_percent = float(input("Enter discount percentage: "))
        discount, final = calculate_discount(total, discount_percent)
        print(f"Discount: {discount:.2f}")
        print(f"Final amount: {final:.2f}")
    except ValueError as e:
        print(f"Error: {e}")