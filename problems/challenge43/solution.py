def number_to_words(num):
    """
    Convert a number to words.
    
    Args:
        num (int): The number to convert
        
    Returns:
        str: Words representation
        
    Raises:
        ValueError: If num is negative or not integer
    """
    if not isinstance(num, int) or num < 0:
        raise ValueError("Number must be a non-negative integer")
    
    if num == 0:
        return "Zero"
    
    words = {
        0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    
    result = []
    for digit in str(num):
        result.append(words[int(digit)])
    
    return ' '.join(result)

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(number_to_words(num))
    except ValueError as e:
        print(f"Error: {e}")