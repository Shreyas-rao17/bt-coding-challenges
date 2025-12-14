"""
Display series 4,16,36,64... up to N
"""

def generate_series(n):
    """
    Generate squares of even numbers up to n.
    """
    series = []
    i = 1
    while True:
        term = (2 * i) ** 2
        if term > n:
            break
        series.append(term)
        i += 1
    return series

if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        series = generate_series(n)
        print(", ".join(map(str, series)))
    except ValueError:
        print("Invalid input.")