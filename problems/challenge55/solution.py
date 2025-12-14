def binary_search(arr, target):
    """
    Perform binary search on sorted array.
    
    Args:
        arr (list): Sorted list of integers
        target (int): Element to search
        
    Returns:
        int: Index if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    try:
        n = int(input("Enter n: "))
        arr = []
        for i in range(n):
            elem = int(input(f"Enter element {i+1}: "))
            arr.append(elem)
        arr.sort()  # Assume sorted
        target = int(input("Enter element to search: "))
        index = binary_search(arr, target)
        if index != -1:
            print(f"Element found at index {index}")
        else:
            print("Element not found")
    except ValueError:
        print("Invalid input.")