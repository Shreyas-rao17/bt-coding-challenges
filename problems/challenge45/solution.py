def separate_whole_fraction(value):
    """
    Separate whole and fractional parts of a double value.
    
    Args:
        value (float): The value to separate
        
    Returns:
        tuple: (whole, fraction)
    """
    whole = int(value)
    fraction = value - whole
    return whole, fraction

if __name__ == "__main__":
    try:
        value = float(input("Enter a double value: "))
        whole, fraction = separate_whole_fraction(value)
        print(f"Whole part: {whole}")
        print(f"Fractional part: {fraction}")
    except ValueError:
        print("Invalid input. Please enter a number.")