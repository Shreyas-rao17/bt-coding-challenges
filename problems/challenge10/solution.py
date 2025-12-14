"""
Student report card calculation.
"""

def calculate_report_card(name, score1, score2, score3):
    """
    Calculate total, average, and class for student.

    Args:
        name (str): Student name
        score1, score2, score3 (float): Subject scores

    Returns:
        dict: {'name': name, 'total': total, 'average': avg, 'class': class_str}

    Raises:
        ValueError: If invalid inputs
    """
    try:
        scores = [float(score1), float(score2), float(score3)]
    except (ValueError, TypeError):
        raise ValueError("Scores must be numbers.")

    for score in scores:
        if not (0 <= score <= 100):
            raise ValueError("Scores must be between 0 and 100.")

    total = sum(scores)
    average = total / 3

    if average >= 60:
        class_str = "1st Class"
    elif average >= 50:
        class_str = "2nd Class"
    elif average >= 35:
        class_str = "Pass Class"
    else:
        class_str = "Fail"

    return {
        'name': name,
        'total': total,
        'average': round(average, 2),
        'class': class_str
    }

if __name__ == "__main__":
    try:
        name = input("Enter student name: ")
        score1 = input("Enter score 1: ")
        score2 = input("Enter score 2: ")
        score3 = input("Enter score 3: ")
        result = calculate_report_card(name, score1, score2, score3)
        print(f"Name: {result['name']}")
        print(f"Total: {result['total']}")
        print(f"Average: {result['average']}")
        print(f"Class: {result['class']}")
    except ValueError as e:
        print(f"Error: {e}")