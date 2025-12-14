def create_2d_array(rows, cols):
    """
    Create and display 2D array row-wise.
    
    Args:
        rows (int): Number of rows
        cols (int): Number of columns
        
    Returns:
        list: 2D array
        
    Raises:
        ValueError: If rows or cols invalid
    """
    if not isinstance(rows, int) or rows <= 0 or not isinstance(cols, int) or cols <= 0:
        raise ValueError("Rows and cols must be positive integers")
    
    arr = []
    for i in range(rows):
        row = []
        for j in range(cols):
            elem = int(input(f"Enter element [{i}][{j}]: "))
            row.append(elem)
        arr.append(row)
    return arr

def display_2d_array(arr):
    """
    Display 2D array row-wise.
    
    Args:
        arr (list): 2D array
    """
    for row in arr:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    try:
        rows = int(input("Enter rows: "))
        cols = int(input("Enter cols: "))
        arr = create_2d_array(rows, cols)
        print("2D Array:")
        display_2d_array(arr)
    except ValueError as e:
        print(f"Error: {e}")