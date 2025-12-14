def sum_2d_array(arr):
    """
    Compute sum of all elements in 2D array.
    
    Args:
        arr (list): 2D array
        
    Returns:
        int: Sum
    """
    return sum(sum(row) for row in arr)

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
        total = sum_2d_array(arr)
        print(f"Sum: {total}")
    except ValueError:
        print("Invalid input.")