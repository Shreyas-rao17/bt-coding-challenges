"""
Display series 1,5,9,13,21,25,29,37,41... up to N
"""

def generate_series(n):
    """
    Generate the series up to n.
    """
    series = []
    current = 1
    series.append(current)
    increments = [4,4,4,8]
    idx = 0
    while True:
        current += increments[idx % 4]
        if current > n:
            break
        series.append(current)
        idx += 1
    return series

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        series = generate_series(n)
        print(", ".join(map(str, series)))
    except ValueError:
        print("Invalid input.")