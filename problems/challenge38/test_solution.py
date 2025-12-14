"""
Tests for Challenge 38: Printing number Increasing Pattern
"""

import io
import sys
from solution import print_number_increasing

def test_n1():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_number_increasing(1)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "1\n"

def test_n3():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_number_increasing(3)
    sys.stdout = sys.__stdout__
    expected = "1\n22\n333\n"
    assert captured_output.getvalue() == expected

def test_n0():
    try:
        print_number_increasing(0)
        assert False
    except ValueError as e:
        assert "N must be a positive integer" in str(e)