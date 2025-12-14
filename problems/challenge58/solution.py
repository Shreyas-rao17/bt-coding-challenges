def search_2d_array(arr, target):
    """
    Check if element exists in 2D array.
    
    Args:
        arr (list): 2D array
        target (int): Element to search
        
    Returns:
        bool: True if found
    """
    for row in arr:
        if target in row:
            return True
    return False

if __name__ == "__main__":
    try:
        rows = int(input("Enter rows: "))
        cols = int(input("Enter cols: "))
        arr = []
        for i in range(rows):
            row = []
            for j in range(cols):
                elem = int(input(f"Enter element [{i}][{j}]: "))
                row.append(elem)
            arr.append(row)
        target = int(input("Enter element to search: "))
        found = search_2d_array(arr, target)
        if found:
            print("Element exists")
        else:
            print("Element does not exist")
    except ValueError:
        print("Invalid input.")