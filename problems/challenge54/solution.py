def sort_array(arr, order):
    """
    Sort the array in ascending or descending order.
    
    Args:
        arr (list): List of integers
        order (str): 'asc' or 'desc'
        
    Returns:
        list: Sorted array
        
    Raises:
        ValueError: If order is invalid
    """
    if order.lower() == 'asc':
        return sorted(arr)
    elif order.lower() == 'desc':
        return sorted(arr, reverse=True)
    else:
        raise ValueError("Order must be 'asc' or 'desc'")

if __name__ == "__main__":
    try:
        n = int(input("Enter n: "))
        arr = []
        for i in range(n):
            elem = int(input(f"Enter element {i+1}: "))
            arr.append(elem)
        order = input("Enter order (asc/desc): ").strip()
        sorted_arr = sort_array(arr, order)
        print(f"Sorted array: {sorted_arr}")
    except ValueError as e:
        print(f"Error: {e}")