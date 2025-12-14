def search_element(arr, target):
    """
    Search for an element in the array.
    
    Args:
        arr (list): List of integers
        target (int): Element to search
        
    Returns:
        int: Index if found, -1 otherwise
    """
    try:
        return arr.index(target)
    except ValueError:
        return -1

if __name__ == "__main__":
    try:
        n = int(input("Enter n: "))
        arr = []
        for i in range(n):
            elem = int(input(f"Enter element {i+1}: "))
            arr.append(elem)
        target = int(input("Enter element to search: "))
        index = search_element(arr, target)
        if index != -1:
            print(f"Element found at index {index}")
        else:
            print("Element not found")
    except ValueError:
        print("Invalid input.")