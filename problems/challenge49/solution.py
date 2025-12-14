def min_array(arr):
    """
    Find minimum value in array.
    
    Args:
        arr (list): List of integers
        
    Returns:
        int: Minimum value
        
    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")
    return min(arr)

if __name__ == "__main__":
    try:
        n = int(input("Enter n: "))
        arr = []
        for i in range(n):
            elem = int(input(f"Enter element {i+1}: "))
            arr.append(elem)
        minimum = min_array(arr)
        print(f"Minimum: {minimum}")
    except ValueError as e:
        print(f"Error: {e}")