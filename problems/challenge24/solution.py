"""
Display series 1,1,2,3,5,8,13,21... up to N
"""

def generate_series(n):
    """
    Generate Fibonacci series up to n.
    """
    series = []
    a, b = 1, 1
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        series = generate_series(n)
        print(", ".join(map(str, series)))
    except ValueError:
        print("Invalid input.")