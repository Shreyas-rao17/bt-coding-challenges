"""
Tests for Challenge 43: Convert Number to Words
"""

from solution import number_to_words

def test_270176():
    assert number_to_words(270176) == "Two Seven Zero One Seven Six"

def test_0():
    assert number_to_words(0) == "Zero"

def test_1():
    assert number_to_words(1) == "One"

def test_123():
    assert number_to_words(123) == "One Two Three"

def test_negative():
    try:
        number_to_words(-1)
        assert False
    except ValueError as e:
        assert "non-negative integer" in str(e)

def test_float():
    try:
        number_to_words(1.5)
        assert False
    except ValueError as e:
        assert "non-negative integer" in str(e)