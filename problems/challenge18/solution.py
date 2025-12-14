"""
Display series 1,3,5,... up to N
"""

def generate_series(n):
    """
    Generate odd numbers up to n.
    """
    return [i for i in range(1, n+1, 2)]

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        series = generate_series(n)
        print(", ".join(map(str, series)))
    except ValueError:
        print("Invalid input.")