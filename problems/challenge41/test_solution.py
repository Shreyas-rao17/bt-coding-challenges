"""
Tests for Challenge 41: Printing Pattern of Perfect Squares with Alternating Signs
"""

import io
import sys
from solution import print_perfect_squares_pattern

def test_n1():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_perfect_squares_pattern(1)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "1\n"

def test_n2():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_perfect_squares_pattern(2)
    sys.stdout = sys.__stdout__
    expected = "1\n-4 9\n"
    assert captured_output.getvalue() == expected

def test_n3():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_perfect_squares_pattern(3)
    sys.stdout = sys.__stdout__
    expected = "1\n-4 9\n-16 25 -36\n"
    assert captured_output.getvalue() == expected

def test_n0():
    try:
        print_perfect_squares_pattern(0)
        assert False
    except ValueError as e:
        assert "N must be a positive integer" in str(e)