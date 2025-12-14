def sum_array(arr):
    """
    Calculate sum of array elements.
    
    Args:
        arr (list): List of integers
        
    Returns:
        int: Sum
    """
    return sum(arr)

if __name__ == "__main__":
    try:
        n = int(input("Enter n: "))
        arr = []
        for i in range(n):
            elem = int(input(f"Enter element {i+1}: "))
            arr.append(elem)
        total = sum_array(arr)
        print(f"Sum: {total}")
    except ValueError:
        print("Invalid input.")