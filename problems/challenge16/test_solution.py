"""
Tests for input validation.
"""

from solution import validate_inputs

def test_valid_inputs():
    errors = validate_inputs("John Doe", "E12345", "50000", "10000", "10")
    assert errors == []

def test_invalid_name_empty():
    errors = validate_inputs("", "E12345", "50000", "10000", "10")
    assert "Name" in str(errors)

def test_invalid_name_numbers():
    errors = validate_inputs("John123", "E12345", "50000", "10000", "10")
    assert "Name" in str(errors)

def test_invalid_empid_short():
    errors = validate_inputs("John", "E12", "50000", "10000", "10")
    assert "EmpID" in str(errors)

def test_invalid_basic_negative():
    errors = validate_inputs("John", "E12345", "-50000", "10000", "10")
    assert "Basic salary" in str(errors)

def test_invalid_allowances_negative():
    errors = validate_inputs("John", "E12345", "50000", "-10000", "10")
    assert "Special allowances" in str(errors)

def test_invalid_bonus_over():
    errors = validate_inputs("John", "E12345", "50000", "10000", "150")
    assert "Bonus percentage" in str(errors)