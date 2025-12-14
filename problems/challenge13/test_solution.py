"""
Tests for tax and rebate.
"""

from solution import calculate_tax_and_cess

def test_no_tax():
    tax, cess, total = calculate_tax_and_cess(200000)
    assert tax == 0
    assert cess == 0
    assert total == 0

def test_rebate():
    tax, cess, total = calculate_tax_and_cess(650000)
    assert tax == 0
    assert cess == 0
    assert total == 0

def test_normal_tax():
    tax, cess, total = calculate_tax_and_cess(750000)
    assert tax == 30000  # 5%*3L + 10%*1.5L
    assert cess == 1200
    assert total == 31200