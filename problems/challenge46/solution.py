def reverse_number(num):
    """
    Reverse the digits of a number.
    
    Args:
        num (int): The number to reverse
        
    Returns:
        int: The reversed number
        
    Raises:
        ValueError: If num is not integer
    """
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    
    if num == 0:
        return 0
    
    sign = 1 if num >= 0 else -1
    num = abs(num)
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return sign * reversed_num

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        reversed_num = reverse_number(num)
        print(f"Reverse: {reversed_num}")
    except ValueError as e:
        print(f"Error: {e}")