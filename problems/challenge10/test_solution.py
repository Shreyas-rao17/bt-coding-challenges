"""
Tests for student report card.
"""

import pytest
from solution import calculate_report_card

def test_first_class():
    result = calculate_report_card("Alice", 70, 80, 90)
    assert result['total'] == 240
    assert result['average'] == 80.0
    assert result['class'] == "1st Class"

def test_second_class():
    result = calculate_report_card("Bob", 55, 60, 50)
    assert result['total'] == 165
    assert result['average'] == 55.0
    assert result['class'] == "2nd Class"

def test_pass_class():
    result = calculate_report_card("Charlie", 40, 45, 35)
    assert result['total'] == 120
    assert result['average'] == 40.0
    assert result['class'] == "Pass Class"

def test_fail():
    result = calculate_report_card("David", 20, 30, 25)
    assert result['total'] == 75
    assert result['average'] == 25.0
    assert result['class'] == "Fail"

def test_boundary_60():
    result = calculate_report_card("Eve", 60, 60, 60)
    assert result['class'] == "1st Class"

def test_boundary_50():
    result = calculate_report_card("Frank", 50, 50, 50)
    assert result['class'] == "2nd Class"

def test_boundary_35():
    result = calculate_report_card("Grace", 35, 35, 35)
    assert result['class'] == "Pass Class"

def test_invalid_score_high():
    with pytest.raises(ValueError, match="Scores must be between 0 and 100"):
        calculate_report_card("Hank", 101, 50, 50)

def test_invalid_score_negative():
    with pytest.raises(ValueError, match="Scores must be between 0 and 100"):
        calculate_report_card("Ivy", -5, 50, 50)

def test_non_numeric_score():
    with pytest.raises(ValueError, match="Scores must be numbers"):
        calculate_report_card("Jack", "abc", 50, 50)