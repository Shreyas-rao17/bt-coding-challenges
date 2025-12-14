"""
Test cases for swapping two numbers.
"""

import pytest
from solution import swap_numbers

def test_swap_integers():
    a, b = swap_numbers(5, 10)
    assert a == 10
    assert b == 5

def test_swap_floats():
    a, b = swap_numbers(1.5, 2.5)
    assert a == 2.5
    assert b == 1.5

def test_swap_same_values():
    a, b = swap_numbers(7, 7)
    assert a == 7
    assert b == 7

def test_swap_negatives():
    a, b = swap_numbers(-3, 4)
    assert a == 4
    assert b == -3

def test_swap_zero():
    a, b = swap_numbers(0, 5)
    assert a == 5
    assert b == 0