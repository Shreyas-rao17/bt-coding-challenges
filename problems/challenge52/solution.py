def count_odd_even(arr):
    """
    Count odd and even numbers in array.
    
    Args:
        arr (list): List of integers
        
    Returns:
        tuple: (odd_count, even_count)
    """
    odd = sum(1 for x in arr if x % 2 != 0)
    even = len(arr) - odd
    return odd, even

if __name__ == "__main__":
    try:
        n = int(input("Enter n: "))
        arr = []
        for i in range(n):
            elem = int(input(f"Enter element {i+1}: "))
            arr.append(elem)
        odd, even = count_odd_even(arr)
        print(f"Odd numbers: {odd}")
        print(f"Even numbers: {even}")
    except ValueError:
        print("Invalid input.")