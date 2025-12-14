"""
Display series 1,2,4,7,11,16,22... up to N
"""

def generate_series(n):
    """
    Generate cumulative sums up to n.
    """
    series = []
    total = 0
    i = 1
    while True:
        total += i
        if total > n:
            break
        series.append(total)
        i += 1
    return series

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        series = generate_series(n)
        print(", ".join(map(str, series)))
    except ValueError:
        print("Invalid input.")