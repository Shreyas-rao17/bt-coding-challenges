"""
Tests for Challenge 42: Printing Pattern of Factorials
"""

import io
import sys
from solution import print_factorials_pattern

def test_n1():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_factorials_pattern(1)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "1\n"

def test_n2():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_factorials_pattern(2)
    sys.stdout = sys.__stdout__
    expected = "1\n1 2\n"
    assert captured_output.getvalue() == expected

def test_n3():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_factorials_pattern(3)
    sys.stdout = sys.__stdout__
    expected = "1\n1 2\n6 24 120\n"
    assert captured_output.getvalue() == expected

def test_n0():
    try:
        print_factorials_pattern(0)
        assert False
    except ValueError as e:
        assert "N must be a positive integer" in str(e)