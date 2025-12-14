"""
Tests for tax calculator.
"""

from solution import (calculate_gross_salary, calculate_taxable_income, 
                      calculate_tax, calculate_net_salary, generate_report)

def test_gross_salary():
    gross_monthly, annual_gross = calculate_gross_salary(50000, 10000, 10)
    assert gross_monthly == 60000
    assert annual_gross == 800000  # 12*60000 / 0.9

def test_taxable_income():
    taxable = calculate_taxable_income(600000)
    assert taxable == 550000  # 600000 - 50000

def test_tax_low_income():
    tax, cess, total = calculate_tax(200000)
    assert tax == 0
    assert cess == 0
    assert total == 0

def test_tax_rebate():
    tax, cess, total = calculate_tax(650000)
    assert tax == 0  # rebate
    assert cess == 0
    assert total == 0

def test_tax_normal():
    tax, cess, total = calculate_tax(750000)
    # Taxable 750000
    # 0-3L:0, 3-6L:5% on 3L=15000, 6-9L:10% on 1.5L=15000, total 30000
    assert tax == 30000
    cess = 30000 * 0.04
    assert cess == 1200
    assert total == 31200

def test_net_salary():
    net = calculate_net_salary(800000, 26000)
    assert net == 774000

def test_generate_report():
    report = generate_report("John", "123", 50000, 10000, 10)
    assert "John" in report
    assert "123" in report
    assert "Annual Net Salary" in report