def accept_array(n):
    """
    Accept n and store elements into an array.
    
    Args:
        n (int): Size of array
        
    Returns:
        list: The array
        
    Raises:
        ValueError: If n is not positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    
    arr = []
    for i in range(n):
        while True:
            try:
                elem = int(input(f"Enter element {i+1}: "))
                arr.append(elem)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return arr

if __name__ == "__main__":
    try:
        n = int(input("Enter n: "))
        arr = accept_array(n)
        print(f"Array: {arr}")
    except ValueError as e:
        print(f"Error: {e}")