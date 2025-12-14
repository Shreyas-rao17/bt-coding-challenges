"""
Tests for Challenge 28: Membership Discounts
"""

from solution import apply_membership_discount

def test_member_discount():
    final_total, discount, explanation = apply_membership_discount(10000, True)
    assert final_total == 9800
    assert discount == 200
    assert "2% membership discount applied: ₹200.00" in explanation

def test_non_member():
    final_total, discount, explanation = apply_membership_discount(10000, False)
    assert final_total == 10000
    assert discount == 0
    assert explanation == ""

def test_zero_total_member():
    final_total, discount, explanation = apply_membership_discount(0, True)
    assert final_total == 0
    assert discount == 0
    assert explanation == ""