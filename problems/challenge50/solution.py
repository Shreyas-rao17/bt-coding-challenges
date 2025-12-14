def max_array(arr):
    """
    Find maximum value in array.
    
    Args:
        arr (list): List of integers
        
    Returns:
        int: Maximum value
        
    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    return max(arr)

if __name__ == "__main__":
    try:
        n = int(input("Enter n: "))
        arr = []
        for i in range(n):
            elem = int(input(f"Enter element {i+1}: "))
            arr.append(elem)
        maximum = max_array(arr)
        print(f"Maximum: {maximum}")
    except ValueError as e:
        print(f"Error: {e}")