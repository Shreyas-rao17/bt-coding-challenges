"""
Display series 1,2,3,...N
"""

def generate_series(n):
    """
    Generate list from 1 to n.
    """
    return list(range(1, n+1))

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        series = generate_series(n)
        print(", ".join(map(str, series)))
    except ValueError:
        print("Invalid input.")