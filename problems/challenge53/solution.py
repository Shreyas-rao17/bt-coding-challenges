def reverse_array(arr):
    """
    Reverse the array.
    
    Args:
        arr (list): List of integers
        
    Returns:
        list: Reversed array
    """
    return arr[::-1]

if __name__ == "__main__":
    try:
        n = int(input("Enter n: "))
        arr = []
        for i in range(n):
            elem = int(input(f"Enter element {i+1}: "))
            arr.append(elem)
        reversed_arr = reverse_array(arr)
        print(f"Reversed array: {reversed_arr}")
    except ValueError:
        print("Invalid input.")