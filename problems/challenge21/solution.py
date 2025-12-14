"""
Display series 1,4,9,25,36,49,81... up to N
"""

def generate_series(n):
    """
    Generate squares of numbers not divisible by 4 up to n.
    """
    series = []
    i = 1
    while True:
        if i % 4 != 0:
            term = i ** 2
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