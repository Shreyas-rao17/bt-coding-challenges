"""
Display series 1,4,7,12,23... up to N
"""

def generate_series(n):
    """
    Generate the series up to n.
    """
    series = []
    current = 1
    series.append(current)
    i = 0
    while True:
        increment = (1 << i) + 1  # 2^i +1
        current += increment
        if current > n:
            break
        series.append(current)
        i += 1
    return series

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        series = generate_series(n)
        print(", ".join(map(str, series)))
    except ValueError:
        print("Invalid input.")