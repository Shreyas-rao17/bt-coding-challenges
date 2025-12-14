"""
Tests for Challenge 56: 2D display row-wise
"""

import io
import sys
from solution import display_2d_array

def test_display():
    arr = [[1, 2], [3, 4]]
    captured_output = io.StringIO()
    sys.stdout = captured_output
    display_2d_array(arr)
    sys.stdout = sys.__stdout__
    expected = "1 2\n3 4\n"
    assert captured_output.getvalue() == expected

def test_single():
    arr = [[5]]
    captured_output = io.StringIO()
    sys.stdout = captured_output
    display_2d_array(arr)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "5\n"