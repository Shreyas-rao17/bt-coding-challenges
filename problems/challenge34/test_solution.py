"""
Tests for Challenge 34: Printing Star Pattern
"""

import io
import sys
from solution import print_star_pattern

def test_n1():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_star_pattern(1)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "*\n"

def test_n3():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_star_pattern(3)
    sys.stdout = sys.__stdout__
    expected = "***\n***\n***\n"
    assert captured_output.getvalue() == expected

def test_n0():
    try:
        print_star_pattern(0)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "N must be a positive integer" in str(e)

def test_negative():
    try:
        print_star_pattern(-1)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "N must be a positive integer" in str(e)

def test_float():
    try:
        print_star_pattern(2.5)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "N must be a positive integer" in str(e)