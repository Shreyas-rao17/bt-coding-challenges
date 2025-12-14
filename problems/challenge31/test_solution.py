"""
Tests for Challenge 31: Payment Mode Rules
"""

from solution import apply_payment_surcharge

def test_cash():
    payable, surcharge = apply_payment_surcharge(10000, "Cash")
    assert payable == 10000
    assert surcharge == 0

def test_credit_card():
    payable, surcharge = apply_payment_surcharge(10000, "Credit Card")
    assert payable == 10200
    assert surcharge == 200

def test_credit_card_case_insensitive():
    payable, surcharge = apply_payment_surcharge(5000, "credit card")
    assert payable == 5100
    assert surcharge == 100

def test_other_payment():
    payable, surcharge = apply_payment_surcharge(10000, "UPI")
    assert payable == 10000
    assert surcharge == 0